import streamlit as st
from repositories.database import add_activity
from services.coaching import resume_review
from services.groq_provider import available, generate
st.title("Resume Assistant")
st.caption("Fact-preserving support only. This demo does not save your pasted resume or job description.")
resume=st.text_area("Paste your resume text", height=220)
job=st.text_area("Paste the target job description", height=180)
use_groq=st.checkbox("Use Groq for additional wording guidance", disabled=not available(), help="Requires GROQ_API_KEY. Your pasted text will be sent to Groq only if selected.")
if st.button("Review alignment"):
    if not resume or not job: st.error("Paste both your resume and a target job description.")
    else:
        st.subheader("Truthful edit guidance")
        for note in resume_review(resume,job): st.write("•",note)
        if use_groq:
            try:
                response=generate(f"Provide concise, fact-preserving resume wording guidance for this resume:\n{resume}\n\nTarget job description:\n{job}")
                if response: st.subheader("Groq wording guidance"); st.write(response)
                else: st.info("Groq did not return usable text; deterministic guidance remains available.")
            except Exception:
                st.warning("Groq is unavailable. Your deterministic fact-preserving guidance is still shown.")
        if st.button("Record resume review in progress"): add_activity("Resume review","Fact-preserving alignment review")
