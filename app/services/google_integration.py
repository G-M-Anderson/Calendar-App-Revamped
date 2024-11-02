from google_auth_oauthlib.flow import Flow
import os

def google_sign_in():
    # Set up OAuth flow
    flow = Flow.from_client_secrets_file(
        os.path.join(os.getcwd(), 'client_secret.json'),
        scopes=["https://www.googleapis.com/auth/calendar"],
        redirect_uri="http://localhost:5000/auth/callback"
    )
    authorization_url, state = flow.authorization_url()
    return authorization_url
