"""Small SQLite repository; no raw uploaded documents are persisted."""
import json
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "career_readiness.db"

DEFAULT_PROFILE = {
    "name": "Demo Student", "degree": "B.Tech", "branch": "Computer Science",
    "graduation_year": 2027, "cgpa": "", "interests": "data, technology",
    "locations": "Bhopal, Remote", "skills": [
        {"name": "Python", "evidence": "coursework"},
        {"name": "SQL", "evidence": "self-reported"},
    ], "projects": "", "consent": False,
}

def _connect():
    con = sqlite3.connect(DB_PATH)
    con.execute("CREATE TABLE IF NOT EXISTS profile (id INTEGER PRIMARY KEY CHECK(id=1), payload TEXT NOT NULL)")
    con.execute("CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, kind TEXT, title TEXT, completed_at TEXT)")
    return con

def load_profile():
    with _connect() as con:
        row = con.execute("SELECT payload FROM profile WHERE id=1").fetchone()
    return json.loads(row[0]) if row else DEFAULT_PROFILE.copy()

def save_profile(profile):
    with _connect() as con:
        con.execute("INSERT INTO profile(id,payload) VALUES(1,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload", (json.dumps(profile),))

def add_activity(kind, title):
    with _connect() as con:
        con.execute("INSERT INTO activities(kind,title,completed_at) VALUES(?,?,datetime('now'))", (kind, title))

def activities():
    with _connect() as con:
        return con.execute("SELECT kind,title,completed_at FROM activities ORDER BY id DESC").fetchall()

def reset_all():
    with _connect() as con:
        con.execute("DELETE FROM profile"); con.execute("DELETE FROM activities")
