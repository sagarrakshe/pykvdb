from abc import ABC, abstractmethod
from typing import Any, Optional


class Store(ABC):
    """Interface for store."""

    @abstractmethod
    def set(self, key: str, value: int) -> None:
        """Set value of the key."""

    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Get value of the key."""

    @abstractmethod
    def delete(self, key: str) -> None:
        """Delete a key."""

    @abstractmethod
    def incr(self, key: str) -> int:
        """Increment value of key by 1."""

    @abstractmethod
    def incrby(self, key: str, value: int) -> int:
        """Increment value of key by given value."""
