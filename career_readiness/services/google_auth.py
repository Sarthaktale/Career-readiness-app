"""Optional Google OAuth for this prototype.

Authentication is active only when the OAuth values are supplied locally in
`.env`; client secrets are never rendered or stored in SQLite.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

def configured():
    return all(os.getenv(key) for key in ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI"))

def sign_in_url():
    from authlib.integrations.requests_client import OAuth2Session
    client = OAuth2Session(os.environ["GOOGLE_CLIENT_ID"], scope="openid email profile", redirect_uri=os.environ["GOOGLE_REDIRECT_URI"])
    url, state = client.create_authorization_url("https://accounts.google.com/o/oauth2/v2/auth")
    return url, state

def complete_sign_in(authorization_response, expected_state):
    from authlib.integrations.requests_client import OAuth2Session
    client = OAuth2Session(os.environ["GOOGLE_CLIENT_ID"], os.environ["GOOGLE_CLIENT_SECRET"], scope="openid email profile", redirect_uri=os.environ["GOOGLE_REDIRECT_URI"], state=expected_state)
    client.fetch_token("https://oauth2.googleapis.com/token", authorization_response=authorization_response)
    return client.get("https://openidconnect.googleapis.com/v1/userinfo").json()
