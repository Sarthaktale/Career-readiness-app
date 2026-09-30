import re

def resume_review(resume, job_description):
    keywords=[w for w in ["python","sql","excel","power bi","git","data structures"] if w in job_description.casefold()]
    found=[w for w in keywords if w in resume.casefold()]
    missing=[w for w in keywords if w not in resume.casefold()]
    suggestions=[]
    if found: suggestions.append("Bring existing evidence for " + ", ".join(found) + " closer to the relevant project or experience heading.")
    if missing: suggestions.append("Do not claim " + ", ".join(missing) + ". Add them only if you can truthfully describe evidence; otherwise use a learning-plan entry.")
    suggestions.append("Replace vague verbs with factual details you can support. Add metrics only if you can verify them.")
    return suggestions

def interview_feedback(answer):
    words=len(re.findall(r"\w+", answer))
    return {"Relevance": "Needs more detail" if words < 35 else "Addresses the question", "Technical correctness": "Not assessed automatically; verify facts and give a concrete example.", "Structure": "Use Situation → Action → Result." if "result" not in answer.casefold() else "Includes outcome language.", "Clarity": "Add a concise opening sentence." if words < 35 else "Readable length; tighten any repetition.", "Improvement": "Name the tools you actually used and one verifiable outcome—never invent either."}
