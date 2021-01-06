from typing import Dict, Any, Optional

from store import Store


class InMemory(Store):
    """InMemory implementation of Store."""

    def __init__(self):
        self.store = {}

    def __exists(self, key) -> bool:
        """Return true if key exists else false."""
        return True if self.store.get(key, None) else False

    def set(self, key: str, value: int) -> None:
        """Set a key."""
        self.store[key] = value

    def get(self, key: str) -> Optional[Any]:
        """Get the key value."""
        return self.store.get(key) if self.__exists(key) else None

    def delete(self, key: str) -> None:
        """Delete the key."""
        del self.store[key]

    def incr(self, key: str) -> int:
        """Increment a key."""
        if not self.__exists(key):
            self.store[key] = 0
        self.store[key] += 1

        return self.store[key]

    def incrby(self, key: str, value: int) -> int:
        """Increment a key by given value."""
        if not self.__exists(key):
            self.store[key] = 0
        self.store[key] += value

        return self.store[key]
