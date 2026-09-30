import streamlit as st
import os
from urllib.parse import urlencode
from services.google_auth import configured, sign_in_url, complete_sign_in

st.title("Sign in")
if st.session_state.get("user"):
    st.success(f"Signed in as {st.session_state.user.get('email', 'Google user')}")
    if st.button("Sign out"): st.session_state.pop("user"); st.query_params.clear(); st.rerun()
elif not configured():
    st.info("Google sign-in is ready to configure. Add the Google OAuth client ID, secret, and registered redirect URI to the local `.env` file, then restart the app.")
else:
    params=st.query_params
    if params.get("code") and params.get("state"):
        try:
            response_url=os.environ["GOOGLE_REDIRECT_URI"] + "?" + urlencode({"code": params["code"], "state": params["state"]})
            st.session_state.user=complete_sign_in(response_url, st.session_state.get("oauth_state"))
            st.query_params.clear(); st.rerun()
        except Exception:
            st.error("Google sign-in could not be completed. Check the registered redirect URI and try again.")
    else:
        url, state=sign_in_url(); st.session_state.oauth_state=state
        st.link_button("Continue with Google", url, type="primary")
