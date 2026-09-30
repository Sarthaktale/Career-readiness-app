import streamlit as st
from repositories.database import add_activity
from services.coaching import interview_feedback
st.title("Mock Interview")
role=st.selectbox("Target role",["Data Analyst","Software Developer","Business Analyst"])
questions={"Data Analyst":"How would you check whether a dashboard metric is trustworthy?","Software Developer":"Describe how you would debug a failing feature.","Business Analyst":"How would you clarify an ambiguous stakeholder request?"}
st.info(f"Question: {questions[role]}")
answer=st.text_area("Your answer",height=180)
if st.button("Get rubric feedback"):
    if not answer.strip(): st.error("Write an answer first.")
    else:
        feedback=interview_feedback(answer)
        for criterion, note in feedback.items(): st.markdown(f"**{criterion}:** {note}")
        add_activity("Interview practice",role)
        st.caption("Feedback uses a deterministic rubric, not a judgment of your personality or employability.")
