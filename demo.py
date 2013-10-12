import os
from flask import Flask
from flask_mwoauth import MWOAuth

app = Flask(__name__)
app.secret_key = os.urandom(24)

print """
NOTE: The callback URL you entered when proposing an OAuth consumer
probably did not match the URL under which you are running this development
server. Your redirect back will therefore fail -- please adapt the URL in
your address bar to http://localhost:5000/oauth-callback?oauth_verifier=...etc
"""

consumer_key = raw_input('Consumer key: ')
consumer_secret = raw_input('Consumer secret: ')

mwoauth = MWOAuth(consumer_key=consumer_key, consumer_secret=consumer_secret)
app.register_blueprint(mwoauth.bp)

@app.route("/")
def gcu():
    return "logged in as: " + repr(mwoauth.get_current_user(False)) + "<br>" + \
           "<a href=login>login</a> / <a href=logout>logout</a>"

if __name__=="__main__":
    app.run(debug=True)
