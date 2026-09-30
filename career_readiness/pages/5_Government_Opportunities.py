import streamlit as st
from services.catalog import GOVT
st.title("Government Opportunities")
st.warning("This screen does not claim any current opening. Confirm notices, dates, and eligibility only from the official source.")
for item in GOVT:
    with st.container(border=True):
        st.markdown(f"**[{item['department']}]({item['url']})**")
        st.write(item['post']); st.write(f"Qualification: {item['qualification']}")
        st.write(f"Dates: {item['dates']}")
        st.caption(f"{item['status']} · Source: {item['source']} · last checked: {item['checked']}")
