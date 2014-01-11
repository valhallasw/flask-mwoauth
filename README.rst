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
