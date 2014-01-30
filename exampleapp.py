from flask import Flask, request, redirect, session
from flask import Response
import os
from projectplace import PPClient

app = Flask(__name__)

# This information is obtained upon registration of a new API app at api.projectplace.com
client_id = "c6b706c4923afb79eca667423e92643a"
client_secret = "8b8bd2b352489a83b331742f98343ab4d00d433b"


@app.route("/")
def demo():
    """Step 1: User Authorization.

    Redirect the user Projectplace, where the users needs to
    authenticate using email and password.
    """
    pp_session = PPClient(client_id)
    authorization_url, state = pp_session.authorization_url()

    # State is used to prevent CSRF, save this and send back
    # when fetching access token.
    session['oauth_state'] = state

    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/callback", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from Projectplace to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """

    pp_session = PPClient(client_id, state=session['oauth_state'])
    token = pp_session.fetch_token(client_secret=client_secret,
                                   authorization_response=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how to fetch the user's profile.
    session['oauth_token'] = token

    path = '1/user/me/profile'

    # If the user tried to access a protected resource we saved the
    # url and now is the time to call it.
    if 'path' in session and session['path'] is not None:
        path = session['path']
        session['path'] = None
    print 'api/' + path

    # Redirect to the real API call
    return redirect('api/' + path)


@app.route("/api/<path:path>", methods=["GET"])
def call_api(path):
    """Fetching a protected resource from our API with saved token.
    Eg. '/api/user/me/projects' will fetch the user's projects.
    """

    # If not authorized we do that now and save the path
    if not 'oauth_token' in session:
        session['path'] = path
        return redirect('/')
    pp_session = PPClient(client_id, token=session['oauth_token'])

    response = pp_session.get(path)

    return Response(response.text, mimetype='application/json')


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True, port=5000)
