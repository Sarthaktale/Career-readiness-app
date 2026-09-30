# Career-readiness-app

**Your Career Counselor** is an English Streamlit prototype that helps students explore careers, identify skill gaps, plan learning, review resumes truthfully, practise interviews, and track progress.

The runnable app is in [`career_readiness/`](career_readiness/README.md).

## Quick start

```powershell
cd career_readiness
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Data and secrets

The O*NET CSV data bundle is intentionally excluded from this repository because it is large. To use the optional taxonomy explorer, place it at `data/db_31_0_csv/` beside this README. O*NET is used only as a U.S. occupational taxonomy, not as Indian job-demand data.

Copy `career_readiness/.env.example` to `career_readiness/.env` and set your own provider credentials locally. Never commit API keys or OAuth secrets.
