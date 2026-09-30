# Product Requirements Document (PRD)

## AI-Powered Career Readiness & Employability Platform --- MPOnline Hackathon

### Product goal

Help students move from academic information to an explainable,
practical career-preparation pathway.

### Challenge requirements

1.  Analyze student profiles and academic records.
2.  Recommend career paths.
3.  Identify skill gaps.
4.  Recommend online courses and certifications.
5.  Match internships and jobs.
6.  Generate AI-based resume improvements.
7.  Conduct mock interviews.
8.  Recommend government employment opportunities.

### Target users

-   Students and recent graduates exploring careers and employment.
-   Demo administrator maintaining sample opportunities and course
    listings.

### Core student journey

Profile and academic information → career options → skill gaps →
learning plan → job/internship and government opportunity matching →
resume tailoring → mock interview → progress tracking.

### MVP requirements

-   Student profile, education, skills, projects, interests, preferred
    location/role.
-   Career recommendations with transparent reasons and alternatives.
-   Skill-gap comparison for a selected role.
-   Courses mapped to specific skill gaps.
-   Job/internship listings with source, date, location, requirements,
    and match explanation.
-   Government opportunities with official source links, eligibility,
    deadline, and verification status.
-   Resume tailoring to a selected job description without inventing
    facts.
-   Text-based mock interview with visible feedback rubric.
-   Progress tracker that updates after learning activities or
    assessments.

### Product principles

-   Evidence-based, explainable, India-focused, privacy-aware, and
    honest.
-   Distinguish assessed skills from self-reported and unassessed
    skills.
-   Distinguish eligibility from relevance.
-   Label sample data and heuristic scores.
-   Do not guarantee placement or claim measured impact without
    evidence.

### Out of scope for initial demo

-   Automated job applications.
-   Guaranteed employment predictions.
-   Unpermitted job-board scraping.
-   Fabricated vacancies, deadlines, course details, resume
    achievements, or market statistics.
-   Treating US occupational data as Indian labor-market demand.

### Acceptance criteria

-   A student can complete and edit a profile.
-   Career suggestions include explanations and multiple options.
-   Skill gaps distinguish missing from not assessed.
-   Every course/opportunity has a source URL or is explicitly labeled
    sample/unverified.
-   Job matches show eligibility separately from relevance.
-   Resume suggestions preserve factual claims.
-   Mock interview returns rubric-based feedback.
-   Completing an activity updates progress.
-   API failure does not crash the demo; labeled sample data remains
    available.
