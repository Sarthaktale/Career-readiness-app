import streamlit as st
from repositories.database import load_profile, add_activity
from services.catalog import JOBS
from services.matching import job_match
from integrations.jobs_provider import fetch_jobs
st.title("Jobs & Internships")
live_records, provider_notice = fetch_jobs()
if live_records:
    st.info(f"IndianAPI Jobs is connected. {provider_notice}")
    st.warning("Live provider records are awaiting one-time schema validation before they are shown as job cards. Sample cards remain available below.")
else:
    st.warning(f"Offline/demo mode: sample records are shown. {provider_notice}")
query=st.text_input("Filter by role or location")
for job in JOBS:
    if query.casefold() not in (job['title']+' '+job['location']).casefold(): continue
    eligibility, relevance=job_match(load_profile(),job)
    with st.container(border=True):
        st.markdown(f"**[{job['title']}]({job['url']})** · {job['company']}")
        st.write(f"{job['location']} · {job['experience']}")
        st.write(f"**Eligibility:** {eligibility}")
        st.write(f"**Relevance:** {relevance}")
        st.caption(f"Skills listed: {', '.join(job['skills'])}. Source: {job['source']} · last checked {job['checked']} · {job['status']}")
        if st.button("Save as research item",key=job['title']): add_activity("Opportunity saved",job['title']); st.success("Saved to local progress.")
