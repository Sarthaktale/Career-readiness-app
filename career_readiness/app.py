import streamlit as st
from pathlib import Path
from repositories.database import load_profile, activities
from services.matching import careers

LOGO = Path(__file__).parent / "assets" / "your-career-counselor-logo.png"
st.set_page_config(page_title="Your Career Counselor", page_icon=str(LOGO), layout="wide")
with st.sidebar:
    st.image(str(LOGO), width=92)
    st.markdown("## Your Career Counselor")
    st.caption("English prototype · local-first student guidance")
st.title("Your Career Counselor")
st.caption("A privacy-aware demo. Career-fit indicators are explainable heuristics, not employment predictions.")
profile = load_profile()
completion = sum(bool(profile.get(k)) for k in ["name","degree","branch","graduation_year","interests","locations","skills"]) / 7
left, middle, right = st.columns(3)
left.metric("Profile completion", f"{completion:.0%}")
middle.metric("Recorded skills", len(profile.get("skills", [])))
right.metric("Completed activities", len(activities()))

st.subheader(f"Welcome, {profile.get('name', 'student')}")
if not profile.get("consent"):
    st.warning("Your profile is local to this demo. Review and consent on My Profile before saving personal information.")
st.info("Recommended next action: confirm your profile, then choose a target role in Career Explorer.")

st.subheader("Career paths to explore")
for item in careers(profile)[:3]:
    with st.container(border=True):
        st.markdown(f"**{item['role']}** · heuristic indicator {item['score']}/75")
        st.write(item["summary"])
        st.caption(item["components"])
        st.write("Matching evidence:", ", ".join(item["matched"]) or "none yet")

st.subheader("Data freshness")
st.caption("Opportunities in this offline demo are clearly labeled sample records or official portal links. Confirm availability, dates, and eligibility at the source before acting.")
