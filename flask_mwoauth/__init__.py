#!/usr/bin/env python
# MediaWiki OAuth connector for Flask
#
# Requires flask-oauthlib
#
# (C) 2013 Merlijn van Deen <valhallasw@arctus.nl>
# Licensed under the MIT License // http://opensource.org/licenses/MIT
#
import sys
from future.utils import iteritems
from flask import request, session, redirect, url_for, flash, Blueprint
import mwoauth
import requests
from requests.models import Request
from requests_oauthlib import OAuth1

__version__ = '0.3.61'


class MWOAuth(object):
    def __init__(self,
                 base_url='https://www.mediawiki.org/w',
                 clean_url="Deprecated",
                 default_return_to='index',
                 consumer_key=None, consumer_secret=None,
                 name="Deprecated"):
        if consumer_key is None:
            raise TypeError(
                "MWOAuth() missing 1 required argument: 'consumer_key'")
        if consumer_secret is None:
            raise TypeError(
                "MWOAuth() missing 1 required argument: 'consumer_secret'")
        consumer_token = mwoauth.ConsumerToken(consumer_key, consumer_secret)
        self.default_return_to = default_return_to
        self.script_url = base_url + "/index.php"
        self.api_url = base_url + "/api.php"

        self.handshaker = mwoauth.Handshaker(self.script_url, consumer_token)

        self.bp = Blueprint('mwoauth', __name__)

        @self.bp.route('/logout')
        def logout():
            session['mwoauth_access_token'] = None
            session['mwoauth_username'] = None
            if 'next' in request.args:
                return redirect(request.args['next'])
            return "Logged out!"

        @self.bp.route('/login')
        def login():
            redirect_to, request_token = self.handshaker.initiate()
            keyed_token_name = _str(request_token.key) + '_request_token'
            keyed_next_name = _str(request_token.key) + '_next'
            session[keyed_token_name] = \
                dict(zip(request_token._fields, request_token))

            if 'next' in request.args:
                session[keyed_next_name] = request.args.get('next')
            else:
                session[keyed_next_name] = self.default_return_to

            return redirect(redirect_to)

        @self.bp.route('/oauth-callback')
        def oauth_authorized():
            request_token_key = request.args.get('oauth_token', 'None')
            keyed_token_name = _str(request_token_key) + '_request_token'
            keyed_next_name = _str(request_token_key) + '_next'

            if keyed_token_name not in session:
                raise Exception("OAuth callback failed.  " +
                                "Can't find keyed token in session.  " +
                                "Are cookies disabled?")

            access_token = self.handshaker.complete(
                mwoauth.RequestToken(**session[keyed_token_name]),
                request.query_string)
            session['mwoauth_access_token'] = \
                dict(zip(access_token._fields, access_token))

            next_url = url_for(session[keyed_next_name])
            del session[keyed_next_name]
            del session[keyed_token_name]

            username = self.get_current_user(False)
            flash(u'You were signed in, %s!' % username)

            return redirect(next_url)

    def _prepare_long_request(self, url, api_query):
        """
        Use requests.Request and requests.PreparedRequest to produce the
        body (and boundary value) of a multipart/form-data; POST request as
        detailed in https://www.mediawiki.org/wiki/API:Edit#Large_texts
        """

        partlist = []
        for k, v in iteritems(api_query):
            if k in ('title', 'text', 'summary'):
                # title,  text and summary values in the request
                # should be utf-8 encoded

                part = (k,
                        (None, v.encode('utf-8'),
                         'text/plain; charset=UTF-8',
                         {'Content-Transfer-Encoding': '8bit'}
                         )
                        )
            else:
                part = (k, (None, v))
            partlist.append(part)

        auth1 = OAuth1(
            self.consumer_token.key,
            client_secret=self.consumer_token.secret,
            resource_owner_key=session['mwoauth_access_token']['key'],
            resource_owner_secret=session['mwoauth_access_token']['secret'])
        return Request(
            url=url, files=partlist, auth=auth1, method="post").prepare()

    def request(self, api_query, url=None):
        """
        e.g. {'action': 'query', 'meta': 'userinfo'}. format=json not required
        function returns a python dict that resembles the api's json response
        """
        api_query['format'] = 'json'
        if url is not None:
            api_url = url + "/api.php"
        else:
            api_url = self.api_url

        size = sum([sys.getsizeof(v) for k, v in iteritems(api_query)])

        if size > (1024 * 8):
            # if request is bigger than 8 kB (the limit is somewhat arbitrary,
            # see https://www.mediawiki.org/wiki/API:Edit#Large_texts) then
            # transmit as multipart message

            req = self._prepare_long_request(url=api_url,
                                             api_query=api_query)
            req.send()
            return req.response.text
        else:
            return requests.post(api_url, data=api_query).text

    def get_current_user(self, cached=True):
        if cached:
            return session.get('mwoauth_username')

        # Get user info
        identity = self.handshaker.identify(
            mwoauth.AccessToken(**session['mwoauth_access_token']))

        # Store user info in session
        session['mwoauth_username'] = identity['username']

        return session['mwoauth_username']


def _str(val):
    """
    Ensures that the val is the default str() type for python2 or 3
    """
    if str == bytes:
        if isinstance(val, str):
            return val
        else:
            return str(val)
    else:
        if isinstance(val, str):
            return val
        else:
            return str(val, 'ascii')
