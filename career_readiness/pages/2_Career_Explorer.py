import streamlit as st
from repositories.database import load_profile
from services.matching import careers
st.title("Career Explorer")
st.info("These are transparent starting points, not a prediction of hiring or placement.")
for item in careers(load_profile()):
    with st.expander(f"{item['role']} — heuristic indicator {item['score']}/75", expanded=True):
        st.write(item["summary"]); st.caption(item["components"])
        st.write("Evidence matched:", ", ".join(item["matched"]) or "No listed evidence yet")
        st.write("Skills to explore or assess:", ", ".join(item["gaps"]) or "None in this compact role map")
