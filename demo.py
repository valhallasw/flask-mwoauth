import json
import os
from builtins import input

from flask import Flask

from flask_mwoauth import MWOAuth

app = Flask(__name__)

# Generate a random secret application key
#
# NOTE: this key changes every invocation. In an actual application, the key
# should not change! Otherwise you might get a different secret key for
# different requests, which means you can't read data stored in cookies,
# which in turn breaks OAuth.
#
# So, for an actual application, use app.secret_key = "some long secret key"
# (which you could generate using os.urandom(24))
#
app.secret_key = os.urandom(24)

print("""
NOTE: The callback URL you entered when proposing an OAuth consumer
probably did not match the URL under which you are running this development
server. Your redirect back will therefore fail -- please adapt the URL in
your address bar to http://localhost:5000/oauth-callback?oauth_verifier=...etc
""")

try:
    creds_doc = json.load(open("credentials.do_not_commit.json"))
    consumer_key = creds_doc['consumer_key']
    consumer_secret = creds_doc['consumer_secret']
except FileNotFoundError:
    print('Couldn\'t find "credentials.do_not_commit.json".' +
          'Please manually input credentials.')
    consumer_key = input('Consumer key: ')
    consumer_secret = input('Consumer secret: ')

mwoauth = MWOAuth(consumer_key=consumer_key, consumer_secret=consumer_secret)
app.register_blueprint(mwoauth.bp)


@app.route("/")
def index():
    return "logged in as: " + repr(mwoauth.get_current_user(True)) + \
           "<br> <a href=login>login</a> / " + \
           "<a href=test_query>test_query</a> / " + \
           "<a href=logout>logout</a>"


@app.route("/test_query")
def test_query():
    username = mwoauth.get_current_user(True)
    data = mwoauth.request({'action': "query", "list": "usercontribs",
                            'ucuser': str(username), 'ucprop': "timestamp",
                            'format': "json"})
    return data

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
