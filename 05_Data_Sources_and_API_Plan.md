# Data Sources, APIs & Data Governance Plan

## Data principles

Use official, licensed, or explicitly permitted data. Verify current API
availability, pricing, rate limits, licensing, and redistribution terms
before implementation. Store provenance and freshness. Label
synthetic/demo records.

## O\*NET

Use as a supplemental occupational and skills taxonomy. It is US-focused
and must not be represented as Indian job-demand data. Check current
downloadable database license and attribution requirements. Do not
assume personal API registration is permitted; confirm eligibility and
terms.

## Indian job-posting data

Evaluate IndianAPI Jobs API or another provider. Before depending on it,
verify: - Current access and registration requirements. - Free-tier
limits and pricing. - Fields returned (title, description, skills,
location, dates, employer). - India and state/city coverage. - Posting
freshness and deduplication. - Terms for storage, analysis, display, and
redistribution.

If API access is unavailable, use a permitted sample CSV and label it
"sample/demo data." Do not scrape sites unless terms explicitly permit
the use.

## Government employment data

Explore National Career Service and India's Open Government Data
platform for relevant services/datasets, but verify each specific
dataset/API rather than assuming one exists. For vacancy details,
prioritize official recruitment notifications and official application
portals.

Potential official sources to investigate include UPSC and Madhya
Pradesh recruitment portals. Verify current URLs and notices before
displaying them.

## Courses

Explore SWAYAM/NPTEL and Skill India Digital Hub. Verify course title,
provider, skill coverage, URL, language, fee, duration, certification
details, and availability. Do not fabricate these fields.

## Normalized data fields

### JobPosting

`id, title, company, description, location, work_mode, employment_type, experience, skills, education_requirements, posted_at, closes_at, source_name, source_url, last_checked_at, status, is_sample`

### GovernmentOpportunity

`id, department, post_title, jurisdiction, location, qualification, age_criteria, dates, fees, selection_process, notification_url, application_url, source_name, last_checked_at, status, is_sample`

### Course

`id, title, provider, url, skills_covered, level, language, fee_status, duration, last_checked_at, status, is_sample`

## Skill normalization

Maintain canonical names and curated aliases. Examples: - Python:
`python`, `python programming` - SQL: `sql`,
`structured query language` - Power BI: `powerbi`, `power bi` - Machine
Learning: `ml`, `machine learning` only when context confirms meaning.

Avoid substring matching that creates false positives (for example,
matching the single letter "R" indiscriminately). Use token boundaries
and context.

## Skill-demand metrics

Within a defined collected dataset: - Count distinct postings mentioning
a skill. - Group by role, location, source, and date window when
available. - Posting share = distinct postings containing skill /
eligible postings in selected group. - Display sample size, source, date
range, and geography. - Describe results as "within this dataset," not
all jobs in India. - Deduplicate using provider IDs or a documented
normalized fingerprint.

## Freshness and verification

Every time-sensitive record should include last checked date and source.
Mark expired, unverified, or stale records clearly. Government
opportunity eligibility and deadlines must be grounded in official
notifications.
