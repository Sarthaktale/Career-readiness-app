# AI, Recommendation Logic & Evaluation Specification

## General rule

Use deterministic, explainable logic for matching and eligibility. Use
an LLM for language generation, summarization, resume wording, and
interview feedback where appropriate. Ground factual outputs in stored
records.

## Career recommendations

Inputs: - Education and subject information. - Skills with evidence
type. - Projects/certifications. - Interests and preferences. -
Role-skill mapping. - Optional job-market signals with provenance.

Return multiple roles with explanations and next steps. A heuristic
score is not a probability of employment.

Possible initial configurable heuristic: - Skill overlap: 40% -
Education/subject relevance: 20% - Projects/certification evidence:
15% - Interests/preferences: 15% - Location/work preference: 10%

These weights are design starting points, not validated science. Show
components and allow preference changes.

## Skill-gap logic

For each target role: - Compare required skills with candidate skills. -
Label as demonstrated, self-reported, not assessed, or gap. - Prioritize
based on explicit role importance, job-posting frequency within the
selected dataset, prerequisites, and student timeline. - Explain each
priority and its source.

## Job matching

Produce two distinct outputs: 1. Eligibility: eligible based on known
requirements / not eligible based on explicit requirement /
unknown---verify. 2. Relevance: skills and preference overlap.

Missing data must result in unknown, not assumed eligibility.

## Course matching

Map each course to canonical skills. Recommend courses covering
identified gaps, with verified source URLs and available details. Offer
practical project/assessment alternatives.

## Resume assistant

-   Use only candidate-provided facts.
-   Tailor phrasing to target job description.
-   Never invent metrics, responsibilities, technologies, credentials,
    or outcomes.
-   If a metric is absent, ask the user to supply it or insert a clearly
    marked placeholder.
-   Explain which job requirement each edit addresses.
-   Let user accept/reject suggestions.

## Mock interview

Use a visible rubric: - Relevance to question. - Technical correctness
where objectively assessable. - Structure. - Clarity. -
Specificity/examples. - Suggested improvement.

Ask one question at a time. Feedback should be constructive and
acknowledge uncertainty. Avoid personality, mental-health, or
unsupported competence claims. Provide repeat practice and progress
comparison.

## Evaluation plan

-   Career matching: review sample profiles with human-defined expected
    relevant roles; inspect explanations and false matches.
-   Skill extraction: manually label a test set and measure
    precision/recall if enough examples exist.
-   Eligibility: test missing, conflicting, and explicit requirements.
-   Resume factuality: verify every generated claim against source
    resume.
-   Opportunity freshness: check source, dates, and expired-state
    handling.
-   Interview feedback: use consistent rubric and review sample outputs.
-   Usability: test complete student journey with a small group and
    record issues.

## Acceptance checks

-   No fabricated student claims, vacancies, course facts, deadlines, or
    eligibility.
-   Unassessed skills are not labeled as confirmed gaps.
-   Demand metrics include scope and sample size.
-   Recommendations include explanations.
-   LLM/API outage does not break core profile, matching, and demo
    flows.
