from .catalog import ROLES

def normal(s): return s.strip().casefold()
def profile_skills(profile): return {normal(x["name"]): x for x in profile.get("skills", []) if x.get("name", "").strip()}

def careers(profile):
    known = profile_skills(profile); interests = profile.get("interests", "").casefold(); result=[]
    for name, role in ROLES.items():
        req=role["skills"]; matched=[s for s in req if normal(s) in known]
        skill_score=round(40*len(matched)/len(req))
        education_score=20 if role["degree"].casefold() in profile.get("branch","").casefold() else 8
        interest_score=15 if any(word in interests for word in name.casefold().split()) else 4
        score=skill_score+education_score+interest_score
        result.append({"role":name,"score":score,"matched":matched,"gaps":[s for s in req if s not in matched],"summary":role["summary"],"components":f"skills {skill_score}/40 · education {education_score}/20 · interests {interest_score}/15 · evidence/preferences not yet scored"})
    return sorted(result,key=lambda x:x["score"],reverse=True)

def skill_gap(profile, role):
    known=profile_skills(profile); req=ROLES[role]["skills"]; rows=[]
    for skill, importance in req.items():
        entry=known.get(normal(skill)); evidence=entry.get("evidence") if entry else None
        state=("Demonstrated" if evidence in {"project","coursework","assessment","certification"} else "Self-reported") if entry else "Not yet assessed / gap"
        rows.append({"Skill":skill,"Status":state,"Priority":"High" if importance==3 else "Medium","Reason":f"Role requirement (importance {importance}/3)"})
    return rows

def job_match(profile, job):
    known=profile_skills(profile); overlap=[s for s in job["skills"] if normal(s) in known]
    eligibility="Potential match — verify" if job.get("education") else "Unknown — verify"
    return eligibility, f"Relevant skills: {', '.join(overlap) if overlap else 'none confirmed'}; missing/unassessed: {', '.join(s for s in job['skills'] if s not in overlap) or 'none listed'}."
