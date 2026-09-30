# Implementation Roadmap & Test Plan

## Phase 1 --- Foundation

-   Inspect repository and preserve existing work.
-   Set up Streamlit navigation and configuration.
-   Create data models/repository layer and sample fixtures.
-   Build student profile form and persistence.
-   Add consent/privacy notice and sample-data labels.

**Exit criteria:** Student can create/edit profile; app starts reliably.

## Phase 2 --- Career intelligence

-   Create canonical skill list, aliases, and role-skill mapping.
-   Implement explainable career recommendations.
-   Implement skill-gap analysis with evidence labels.
-   Add tests for normalization and matching.

**Exit criteria:** Selected role displays known skills, gaps, and
rationale.

## Phase 3 --- Learning and opportunities

-   Build course catalog and skill mapping.
-   Add job provider adapter or sample CSV fallback.
-   Add government opportunity records with official source fields.
-   Implement eligibility/relevance separation, filters, and freshness
    labels.

**Exit criteria:** Student sees relevant opportunities with source and
verification status.

## Phase 4 --- AI features

-   Implement resume assistant with factuality constraints.
-   Implement text-based mock interview with rubric feedback.
-   Add LLM adapter and graceful fallback.

**Exit criteria:** Resume edits preserve facts; interview works or
clearly reports provider unavailability.

## Phase 5 --- Progress and demo polish

-   Add learning, assessment, and application tracker.
-   Update skill evidence after assessment/course activity.
-   Add demand charts with dataset scope/sample size.
-   Test end-to-end demo and fix usability issues.

**Exit criteria:** Completing an activity updates progress and relevant
recommendations.

## Test scenarios

1.  Empty profile: no crash; prompt user to add information.
2.  Unassessed skill: display "not assessed," not "missing."
3.  Candidate missing explicit mandatory degree: eligibility marked not
    eligible.
4.  Candidate lacks eligibility information: mark unknown/verify.
5.  Expired vacancy: flagged and not shown as open.
6.  Provider/API unavailable: labeled sample/cached data works.
7.  Resume has no measurable outcome: assistant asks for truthful
    metric; does not invent one.
8.  Course missing source URL: do not present as verified
    recommendation.
9.  Duplicate job posting: deduplicate where possible.
10. Complete demo journey: profile → career → gaps → course →
    opportunity → resume → interview → progress.

## Demo narrative

Problem: Students struggle to connect education, skills, and current
opportunities. Solution: One connected platform provides explainable
career options, targeted learning, verified opportunity discovery,
resume support, and interview practice. Demo: Walk one sample student
through the full journey and show progress updating after a
learning/assessment activity. Impact: Report functional coverage, data
coverage, and user feedback honestly; do not claim placement gains
without evidence.
