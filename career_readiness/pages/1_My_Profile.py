import streamlit as st
from repositories.database import load_profile, save_profile, reset_all

st.title("My Profile")
st.caption("Only enter information you want this local demo to store. Uploaded documents are not collected in this MVP.")
p=load_profile()
with st.form("profile"):
    name=st.text_input("Name", p.get("name", ""))
    degree=st.text_input("Degree", p.get("degree", ""))
    branch=st.text_input("Branch / specialization", p.get("branch", ""))
    year=st.number_input("Graduation year", 2020, 2035, int(p.get("graduation_year",2027)))
    cgpa=st.text_input("CGPA (optional)", p.get("cgpa", ""))
    interests=st.text_input("Interests", p.get("interests", ""))
    locations=st.text_input("Preferred locations / work mode", p.get("locations", ""))
    skills_text=st.text_area("Skills, one per line: Skill | evidence type", "\n".join(f"{x['name']} | {x['evidence']}" for x in p.get("skills", [])), help="Evidence types: self-reported, coursework, assessment, project, certification.")
    projects=st.text_area("Projects or experience (optional)", p.get("projects", ""))
    consent=st.checkbox("I consent to local storage of these profile fields for this demo", value=p.get("consent",False))
    submitted=st.form_submit_button("Save profile")
if submitted:
    skills=[]
    for line in skills_text.splitlines():
        chunks=[x.strip() for x in line.split("|",1)]
        if chunks[0]: skills.append({"name":chunks[0],"evidence":chunks[1].casefold() if len(chunks)>1 else "self-reported"})
    save_profile({"name":name,"degree":degree,"branch":branch,"graduation_year":year,"cgpa":cgpa,"interests":interests,"locations":locations,"skills":skills,"projects":projects,"consent":consent})
    st.success("Profile saved locally.")
if st.button("Delete/reset local demo data"):
    reset_all(); st.success("Local profile and activity records were removed. Refresh this page to see the demo defaults.")
