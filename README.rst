flask-mwoauth
--------------
.. image:: https://pypip.in/v/flask-mwoauth/badge.png
        :target: https://crate.io/packages/flask-mwoauth

.. image:: https://pypip.in/d/flask-mwoauth/badge.png
        :target: https://crate.io/packages/flask-mwoauth
	        

Flask blueprint to run OAuth against MediaWiki's extension:OAuth.

The blueprint adds these uris:
 - /login - runs the OAuth handshake and returns the user to /
 
   - /login?next=/someurl will return the user to /someurl
  
 - /logout - clears the users' access tokens

   - /logout?next=/someurl will return the user to /someurl

 - /oauth-callback - callback from MW to finish the handshake

The users' OAuth key and secret are stored in the session.


In addition, flask-mwoauth adds a few convenience functions:
 - `get_current_user(cached=True)` reports who the current user is. To confirm
   the user is still logged in (e.g. tokens have not been revoked), call it
   with cached=False.
 - `request(api_query)` submits an request through the API, using the users'
   access tokens. E.g. the current user request runs
   `request({'action': 'query', 'meta': 'userinfo'})`.

An example app is implemented in `demo.py`.

Using the example app
---------------------
1. Go to https://www.mediawiki.org/wiki/Special:OAuthConsumerRegistration/propose and fill in the following values:
  - Application name: test app
  - Application description: test app for flask-mwoauth
  - OAuth "callback" URL: http://localhost:5000/oauth-callback
  - Contact email address: <your registered email address>
  - Leave all other values default.
2. Click 'Propose consumer'. You now get a message stating "Your OAuth consumer request has been received. You have been assigned a consumer token of **<consumer key>** and a secret token of **<consumer secret>**. Please record these for future reference."
3.

``` bash
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

4. Go to http://localhost:5000/ and click 'login'.
