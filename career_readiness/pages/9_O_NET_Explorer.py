import streamlit as st
from services.onet_taxonomy import search_occupations, ONET_DIR

st.title("O*NET Taxonomy Explorer")
st.warning("O*NET is a U.S. occupational taxonomy. It is shown for career-language exploration only—not Indian job demand, vacancy availability, or eligibility.")
query=st.text_input("Search an occupation or keyword", placeholder="e.g., data analyst")
if not ONET_DIR.exists(): st.error("The local O*NET CSV folder was not found.")
elif query:
    matches=search_occupations(query)
    if not matches: st.info("No matching local taxonomy record.")
    for item in matches:
        with st.expander(f"{item['Title']} ({item['O*NET-SOC Code']})"):
            st.write(item['Description'])
            st.caption("Source: locally supplied O*NET 31.0 CSV data.")
