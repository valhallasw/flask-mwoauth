flask-mwoauth
--------------
Flask blueprint to run OAuth against MediaWiki's extension:OAuth.

The blueprint adds these uris:
 - /login - runs the OAuth handshake and returns the user to /
   - /login?next=/someurl will return the user to /someurl
 - /logout - clears the users' access tokens
   - /logout?next=/someurl will return the user to /someurl
 - /oauth-callback - callback from MW to finish the handshake

The users' OAuth key and secret are stored in the session.


In addition, flask-mwoauth adds a few convenience functions:

1. `get_current_user(cached=True)` reports who the current user is. To confirm
   the user is still logged in (e.g. tokens have not been revoked), call it
   with cached=False.

2. `request(api_query)` submits an request through the API, using the users' access tokens. For instance,

```
result = request({'action': 'query', 'meta': 'userinfo'})
```

fetches https://www.mediawiki.org/w/api.php?action=query&meta=userinfo and returns the result as Python dict, e.g.

```
{u'batchcomplete': u'', u'query': {u'userinfo': {u'id': 31344, u'name': u'Valhallasw'}}}
```

If you are authorized to access other wikis (e.g. en.wikipedia.org, although you authorized via mediawiki.org), you can run a request there using

```
result = request({'action': 'query', 'meta': 'userinfo'}, url='https://en.wikipedia.org/w/api.php')
```
  
For more information on using the api, please check the api documentation at https://www.mediawiki.org/wiki/API:Main_page
  
The example app
---------------------
An example app is implemented in `demo.py`.

1. Go to https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose and fill in the following values:
  - Application name: test app
  - Application description: test app for flask-mwoauth
  - OAuth "callback" URL: http://localhost:5000/oauth-callback
  - Contact email address: <your registered email address>
  - Leave all other values default.

2. Click 'Propose consumer'. You now get a message stating
  > Your OAuth consumer request has been received.
  >
  >You have been assigned a consumer token of **<consumer key>** and a secret token of **<consumer secret>**. Please record these for future reference."

3. Then
    ```
    $ python setup.py develop
    $ python demo.py
    NOTE: The callback URL you entered when proposing an OAuth consumer
    probably did not match the URL under which you are running this development
    server. Your redirect back will therefore fail -- please adapt the URL in
    your address bar to http://localhost:5000/oauth-callback?oauth_verifier=...etc
    
    Consumer key: <the consumer key you got>
    Consumer secret: <the consumer secret you got>
    ```
    You may need to re-enter the key and secret if the app reloads.

4. Go to [http://localhost:5000/](http://localhost:5000/) and click 'login'.

Projects using flask-mwoauth
----------------------------
To see how flask-mwoauth is used in applications, you can take a look at:
  * [mwoauth-test](https://github.com/CristianCantoro/mwoauth-test/)
  * [gerrit-patch-uploader](https://github.com/valhallasw/gerrit-patch-uploader):
    * [connecting the blueprint](https://github.com/valhallasw/gerrit-patch-uploader/blob/e90e5e3a8930124890c93e9c3174183a3defc794/patchuploader.py#L26),
    * [getting the logged in user](https://github.com/valhallasw/gerrit-patch-uploader/blob/e90e5e3a8930124890c93e9c3174183a3defc794/patchuploader.py#L53)
  * [wikipedia-tags-in-osm](https://github.com/CristianCantoro/wikipedia-tags-in-osm):
    * [querying the wiki](https://github.com/CristianCantoro/wikipedia-tags-in-osm/blob/wikimap/app/wiki.py#L363)
    * [editing a wiki](https://github.com/CristianCantoro/wikipedia-tags-in-osm/blob/wikimap/app/wiki.py#L497)
