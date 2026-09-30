# Technology Stack & Implementation Specification

### Recommended hackathon stack

-   UI: Streamlit.
-   Language: Python.
-   Data processing: Pandas.
-   Database: SQLite for local prototype; PostgreSQL if deployment/team
    needs it.
-   Charts: Plotly or Matplotlib.
-   ML: scikit-learn only for clearly justified tasks; start with
    explainable rules.
-   LLM: provider-agnostic service wrapper for resume suggestions,
    interview feedback, and conversational explanations.
-   Document parsing: PDF/DOCX text extraction; OCR as optional stretch
    feature with user confirmation.
-   Secrets: environment variables or deployment secret manager.
-   Version control: Git.

### Suggested dependencies

Keep dependencies minimal and pin tested versions in `requirements.txt`.
Possible packages: `streamlit`, `pandas`, `plotly`, `python-dotenv`,
`pydantic`, PDF/DOCX parsing libraries, and the chosen LLM SDK.

### Project structure

``` text
career_readiness/
  app.py
  pages/
    1_Profile.py
    2_Career_Explorer.py
    3_Skill_Gaps.py
    4_Learning_Plan.py
    5_Opportunities.py
    6_Resume_Assistant.py
    7_Mock_Interview.py
    8_Progress.py
  services/
    profile_service.py
    career_matcher.py
    skill_gap.py
    course_matcher.py
    job_matcher.py
    government_opportunities.py
    resume_assistant.py
    interview_coach.py
    demand_analytics.py
  repositories/
    database.py
  integrations/
    jobs_provider.py
    llm_provider.py
  utils/
    validation.py
    normalization.py
    dates.py
  data/
    sample_jobs.csv
    sample_courses.csv
    sample_government_opportunities.csv
    role_skills.csv
    skill_aliases.csv
  tests/
  .env.example
  requirements.txt
  README.md
```

### Engineering rules

-   Separate UI, business logic, data access, and external integrations.
-   Use provider adapters so APIs can be replaced without rewriting
    modules.
-   Keep secrets out of source control and logs.
-   Validate user inputs and external data.
-   Add graceful fallback to clearly labeled sample data.
-   Include setup instructions and a `.env.example`.
-   Build incrementally; test each end-to-end path before expanding
    scope.

### Implementation phases

1.  Foundation: navigation, configuration, data models, sample data,
    profile persistence.
2.  Career intelligence: skill taxonomy, aliases, role-skill mapping,
    career matching, skill gaps.
3.  Learning/opportunities: course catalog, jobs adapter, government
    opportunity records, filters.
4.  AI features: resume assistant and text mock interview with fallback
    behavior.
5.  Progress and polish: trackers, demand charts, validation, tests,
    demo walkthrough.

### Environment configuration

Use placeholders in `.env.example`, never real secrets:

``` text
LLM_API_KEY=
JOBS_API_KEY=
DATABASE_URL=sqlite:///career_readiness.db
```

Only include variables for integrations actually implemented.
