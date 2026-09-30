"""IndianAPI Jobs adapter using the documented endpoint and x-api-key header."""
import json
import os
from datetime import date
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

def fetch_jobs():
    url = os.getenv("INDIANAPI_JOBS_URL", "https://jobs.indianapi.in/jobs")
    key = os.getenv("INDIANAPI_JOBS_KEY")
    if not url or not key:
        return [], "Live provider is not configured; showing local sample/demo records."
    request = Request(url, headers={"x-api-key": key, "Accept": "application/json"})
    try:
        with urlopen(request, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, ValueError) as error:
        return [], f"Live provider unavailable ({type(error).__name__}); showing local sample/demo records."
    items = payload.get("data", payload) if isinstance(payload, dict) else payload
    if not isinstance(items, list): return [], "Provider response could not be validated; showing local sample/demo records."
    # The supplied spec does not document field names. Preserve raw records until
    # one authenticated response has been reviewed and explicitly mapped.
    return items, f"Provider returned {len(items)} records on {date.today().isoformat()}; schema verification is pending."
