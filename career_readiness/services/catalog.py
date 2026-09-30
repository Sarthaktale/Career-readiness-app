from datetime import date

TODAY = date.today().isoformat()
ROLES = {
    "Data Analyst": {"skills": {"Python": 3, "SQL": 3, "Excel": 2, "Power BI": 2}, "degree": "Computer", "summary": "Turns data into useful reports and decisions."},
    "Software Developer": {"skills": {"Python": 3, "SQL": 2, "Git": 2, "Data Structures": 3}, "degree": "Computer", "summary": "Builds and maintains software products."},
    "Business Analyst": {"skills": {"Excel": 3, "SQL": 2, "Communication": 3, "Power BI": 2}, "degree": "", "summary": "Connects business needs with data and delivery teams."},
}
COURSES = [
 {"title":"NPTEL: Programming in Python", "provider":"NPTEL", "skills":["Python"], "url":"https://nptel.ac.in/courses", "level":"Beginner", "language":"English", "checked":TODAY},
 {"title":"SWAYAM course catalogue", "provider":"SWAYAM", "skills":["SQL", "Data Structures", "Excel"], "url":"https://swayam.gov.in/", "level":"Varies", "language":"English/Hindi", "checked":TODAY},
 {"title":"Microsoft Learn: Power BI", "provider":"Microsoft Learn", "skills":["Power BI"], "url":"https://learn.microsoft.com/training/powerplatform/power-bi/", "level":"Beginner", "language":"English", "checked":TODAY},
]
JOBS = [
 {"title":"Data Analyst Intern", "company":"Sample Analytics Lab", "location":"Bhopal / Hybrid", "skills":["Python","SQL","Excel"], "education":"Any undergraduate degree", "experience":"Student", "source":"Sample/demo listing", "url":"https://example.com/sample-data-analyst", "checked":TODAY, "status":"Sample — verify before applying"},
 {"title":"Junior Python Developer", "company":"Sample Tech Studio", "location":"Remote", "skills":["Python","Git","Data Structures"], "education":"Computer-related degree preferred", "experience":"0–1 years", "source":"Sample/demo listing", "url":"https://example.com/sample-python-developer", "checked":TODAY, "status":"Sample — verify before applying"},
]
GOVT = [
 {"department":"Demo record — not a vacancy", "post":"Check official recruitment portals", "qualification":"Verify in notification", "dates":"No deadline supplied", "source":"Official portal directory", "url":"https://www.ncs.gov.in/", "checked":TODAY, "status":"Needs verification — no opening asserted"},
 {"department":"UPSC", "post":"Official notifications", "qualification":"See notification", "dates":"See official calendar/notice", "source":"UPSC official website", "url":"https://upsc.gov.in/", "checked":TODAY, "status":"Needs verification — no opening asserted"},
]
