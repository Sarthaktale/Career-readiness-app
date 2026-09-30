"""Read only the locally supplied O*NET CSV taxonomy.

O*NET is US-focused and is used here for occupational language/skill discovery,
never as a measure of Indian job demand or eligibility.
"""
import csv
from functools import lru_cache
from pathlib import Path

ONET_DIR = Path(__file__).resolve().parents[2] / "data" / "db_31_0_csv"

@lru_cache(maxsize=1)
def occupations():
    path = ONET_DIR / "occupation_data.csv"
    if not path.exists(): return []
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))

def search_occupations(query, limit=8):
    query = query.casefold().strip()
    if not query: return []
    return [r for r in occupations() if query in (r["Title"] + " " + r["Description"]).casefold()][:limit]
