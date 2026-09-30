# UI/UX Design Specification

## AI-Powered Career Readiness Platform

### Design direction

A trustworthy, student-friendly, mobile-responsive dashboard. Use clear
hierarchy, accessible contrast, plain language, and restrained use of
AI-themed decoration. Avoid presenting heuristic scores as authoritative
predictions.

### Primary navigation

1.  Dashboard
2.  My Profile
3.  Career Explorer
4.  Skill Gap & Learning Plan
5.  Jobs & Internships
6.  Government Opportunities
7.  Resume Assistant
8.  Mock Interview
9.  Progress

### Key screens

#### Dashboard

-   Welcome and profile completion status.
-   Recommended next action.
-   Career paths to explore.
-   Current skill-development goals.
-   Saved opportunities and application status.
-   Recent learning/interview activity.
-   Data freshness notice where market data is shown.

#### Profile & Academic Analyzer

-   Education: degree, branch, graduation year, semester, subject
    marks/grades, CGPA (optional).
-   Skills with proficiency and evidence type: self-reported,
    coursework, assessment, project, certification.
-   Projects, internships, certifications, interests, preferred
    roles/locations.
-   Upload/parse flow must show extracted values for confirmation.
-   Provide edit/delete controls and privacy notice.

#### Career Explorer

-   Show several career paths, not a single verdict.
-   Each card: role summary, matching evidence, relevant skills, gaps,
    data source.
-   Explain score components and label them heuristic, not hiring
    probability.
-   Allow users to change preferences and compare roles.

#### Skill Gap & Learning Plan

-   Sections: demonstrated skills, self-reported skills,
    not-yet-assessed skills, gaps for target role.
-   Priority reason for each gap.
-   Course cards linked to one or more gaps, provider, level, language,
    verified URL, last checked.
-   Include practical project or assessment suggestions.

#### Jobs & Internships

-   Filters: role, location, experience, work mode, posting date.
-   Cards show company, title, location, posted/closing date if known,
    skills, eligibility status, match explanation, source link, last
    checked.
-   Separate "Eligible based on known data," "Potential match---verify,"
    and "Not eligible based on stated requirement."
-   Never infer eligibility from missing data.

#### Government Opportunities

-   Central/state filter; department, post, qualification, age criteria
    if applicable, dates, selection process, official notification link.
-   Prominent status: verified/open, deadline passed, or needs
    verification.
-   Display official source and last-checked timestamp.

#### Resume Assistant

-   Upload/paste resume and target job description.
-   Show original and suggested text side by side.
-   Mark unsupported claims and ask user to provide truthful
    evidence/metrics.
-   Accept/reject edits individually.
-   Explain job-requirement alignment.

#### Mock Interview

-   Select target role, level, interview type, language.
-   One question at a time with answer input.
-   Feedback rubric: relevance, technical correctness when assessable,
    structure, clarity, improvement suggestion.
-   Offer retry and progress comparison; avoid personality/psychological
    judgments.

#### Progress

-   Courses, assessments, projects, resume versions, interview sessions,
    saved/applied opportunities.
-   Show progress over time, not an opaque universal employability
    score.

### UI states

Design loading, empty, error, offline/sample-data, expired listing, and
unverified-data states. Keep API status understandable to students.

### Accessibility

-   Keyboard-friendly controls, descriptive labels, readable typography.
-   Mobile-first layout.
-   Consider English and Hindi localization.
-   Do not rely on color alone to communicate status.
