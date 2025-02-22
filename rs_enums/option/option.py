"""
This module provides an implementation of the Option type, which represents
an optional value that can be either present (Some) or absent (None).
"""

from typing import Generic, Optional
from ..generics import T


class Some(Generic[T]):
    """
    This class represents a value that is present and can be used safely.
    """

    def __init__(self, value: T) -> None:
        self.value: T = value

    def get_value(self) -> T:
        """Return the stored value."""
        return self.value

    def is_present(self) -> bool:
        """Check if the value is present."""
        return self.value is not None


class Option(Generic[T]):
    """
    This class represents an optional value that can be either present (Some)
    or absent (None).
    """

    def __init__(self, value: Optional[T]) -> None:
        """Initialize the Option with a value, which can be Some or None."""
        self.value = Some(value) if value is not None else None

    @classmethod
    def new(cls, value: Optional[T]) -> "Option[T]":
        """Create an Option instance from a value, returning an Option instance even if the value is None."""
        return cls(value)

    def is_some(self) -> bool:
        """Check if the Option contains a value (is not None)."""
        return isinstance(self.value, Some)

    def is_none(self) -> bool:
        """Check if the Option does not contain a value (is None)."""
        return self.value is None

    def unwrap(self) -> T:
        """Return the value if present; raise RuntimeError if None."""
        if self.is_none():
            raise RuntimeError("Value is None")
        return self.value.get_value()

    def expect(self, message: str) -> T:
        """Return the value if present; raise RuntimeError with a message if None."""
        if self.is_none():
            raise RuntimeError(message)
        return self.value.get_value()
