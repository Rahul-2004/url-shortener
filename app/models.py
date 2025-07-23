from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import Dict, Optional

@dataclass
class UrlRecord:
    original: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    clicks: int = 0

class InMemoryDB:
    """
    Thread-safe, process-local key-value store.
    Uses a single lock because write contention is expected
    to be very low for a demo service.
    """

    def __init__(self) -> None:
        self._data: Dict[str, UrlRecord] = {}
        self._lock: Lock = Lock()

    def save(self, code: str, url: str) -> None:
        with self._lock:
            self._data[code] = UrlRecord(original=url)

    def get(self, code: str) -> Optional[UrlRecord]:
        return self._data.get(code)

    def increment_clicks(self, code: str) -> None:
        with self._lock:
            if code in self._data:
                self._data[code].clicks += 1
