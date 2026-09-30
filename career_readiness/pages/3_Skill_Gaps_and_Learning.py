import streamlit as st
import pandas as pd
from repositories.database import load_profile, add_activity
from services.catalog import ROLES, COURSES
from services.matching import skill_gap
st.title("Skill Gap & Learning Plan")
role=st.selectbox("Target role", list(ROLES))
rows=skill_gap(load_profile(),role)
st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)
gaps={r['Skill'] for r in rows if 'gap' in r['Status'].casefold() or 'assessed' in r['Status'].casefold()}
st.subheader("Source-linked learning options")
for course in COURSES:
    mapped=gaps.intersection(course['skills'])
    if mapped:
        with st.container(border=True):
            st.markdown(f"**[{course['title']}]({course['url']})** — {course['provider']}")
            st.write(f"Covers: {', '.join(mapped)} · {course['level']} · {course['language']}")
            st.caption(f"Last checked: {course['checked']}. Confirm availability, language, fees, and certification at the provider.")
            if st.button("Mark completed", key=course['title']): add_activity("Learning", course['title']); st.success("Activity recorded.")
st.info("Practical alternative: build a small, truthful portfolio project that uses one priority skill, then record the evidence in My Profile.")
