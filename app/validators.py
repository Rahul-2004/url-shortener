import re
from urllib.parse import urlparse

ALLOWED_SCHEMES = {"http", "https"}

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        if result.scheme.lower() not in ALLOWED_SCHEMES:
            return False
        # rudimentary host check
        hostname = result.hostname or ""
        if not re.match(r"^[A-Za-z0-9.-]+$", hostname):
            return False
        return True
    except Exception:
        return False
