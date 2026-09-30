# System Architecture

## AI-Powered Career Readiness & Employability Platform

### Architecture goals

-   Modular and testable.
-   One shared student profile across modules.
-   External data sources replaceable through adapters.
-   AI used for language tasks, not as an ungrounded source of factual
    vacancies or eligibility.
-   Functional offline/demo mode.

### Logical layers

1.  **Presentation layer**
    -   Streamlit pages and reusable UI components.
    -   Forms, filters, status indicators, explanations, and progress
        views.
2.  **Application/service layer**
    -   Profile service.
    -   Career matching service.
    -   Skill-gap and learning-plan service.
    -   Job and government-opportunity matching.
    -   Resume assistant.
    -   Mock interview coach.
    -   Progress tracker.
3.  **Domain/data layer**
    -   Student, skills, roles, jobs, courses, government opportunities,
        assessments, activities, and data-source records.
    -   Repository abstraction over SQLite/PostgreSQL or CSV demo
        fixtures.
4.  **Integration layer**
    -   Job provider adapter.
    -   LLM provider adapter.
    -   Course/government source importers.
    -   Each adapter handles authentication, rate limits, parsing,
        validation, and errors.
5.  **Reliability and privacy layer**
    -   Input validation, consent, access controls if accounts are used,
        source provenance, freshness, logging without sensitive content,
        and graceful fallbacks.

### Main data flow

Student enters/uploads profile → values are confirmed and normalized →
profile stored → role-skill mapping and job data queried → career
options and skill gaps calculated → courses/opportunities matched →
resume/interview tools use selected target role → activity outcomes
update profile evidence and progress → recommendations can be
recalculated.

### Suggested entities

-   Student
-   EducationRecord
-   Skill
-   StudentSkill (proficiency, evidence_type, assessed_at)
-   Project
-   CareerRole
-   RoleSkill (importance, source)
-   JobPosting
-   JobSkill
-   Course
-   CourseSkill
-   GovernmentOpportunity
-   ResumeDocument metadata
-   InterviewSession
-   LearningActivity
-   ApplicationTracker
-   DataSource

### Integration contracts

Every external record should preserve: - Source name and URL. -
Retrieved/last-checked timestamp. - Provider ID if available. -
Geographic coverage. - License/terms note where known. -
Verification/status field.

### Failure handling

-   Provider unavailable: show cached or sample records with clear
    label.
-   Invalid external response: reject/flag record; do not silently
    fabricate missing fields.
-   LLM unavailable: provide deterministic templates/rubric or disable
    the AI action with an explanation.
-   Expired listing: mark expired; do not show as currently open.

### Trust boundaries

Treat uploaded resumes, academic documents, job descriptions, and API
text as untrusted input. Never allow embedded content to override
application instructions or expose secrets.
