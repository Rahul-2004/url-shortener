import secrets
import string
from typing import Tuple

from .models import InMemoryDB
from .validators import is_valid_url

CODE_LENGTH = 6
ALPHANUM = string.ascii_letters + string.digits   # 62-symbol alphabet

class UrlShortenerService:
    def __init__(self, db: InMemoryDB) -> None:
        self._db = db

    # ---------- Public API ---------- #

    def shorten(self, long_url: str) -> Tuple[str, str]:
        if not is_valid_url(long_url):
            raise ValueError("invalid URL format")

        # collision-free loop, negligible iterations given 62⁶ space
        while True:
            code = self._generate_code()
            if not self._db.get(code):
                self._db.save(code, long_url)
                return code, long_url

    def resolve(self, code: str) -> str:
        rec = self._db.get(code)
        if not rec:
            raise KeyError("not found")
        self._db.increment_clicks(code)
        return rec.original

    def stats(self, code: str):
        rec = self._db.get(code)
        if not rec:
            raise KeyError("not found")
        return {
            "url": rec.original,
            "clicks": rec.clicks,
            "created_at": rec.created_at.isoformat() + "Z",
        }

    # ---------- Internal helpers ---------- #

    @staticmethod
    def _generate_code() -> str:
        # cryptographically secure + fast
        return "".join(secrets.choice(ALPHANUM) for _ in range(CODE_LENGTH))
