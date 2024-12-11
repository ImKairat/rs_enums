"""
This module provides an implementation of the Option type, which represents 
an optional value that can be either present (Some) or absent (None).
"""

from typing import Any


class Some:
    """
    This class represents a value that is present and can be used safely.
    """
    def __init__(self, value: Any) -> None:
        self.value: Any = value

    def get_value(self) -> Any:
        """Return the stored value."""
        return self.value

    def is_present(self) -> bool:
        """Check if the value is present."""
        return self.value is not None


class Option:
    """
    This class represents an optional value that can be either present (Some) 
    or absent (None).
    """
    def __init__(self, value: Any) -> None:
        """Initialize the Option with a value, which can be Some or None."""
        self.value = Some(value) if value is not None else None

    @classmethod
    def new(cls, value: Any) -> 'Option':
        """Create an Option instance from a value, returning None if the value is None."""
        return cls(Some(value) if value is not None else None)

    def is_some(self) -> bool:
        """Check if the Option contains a value (is not None)."""
        return isinstance(self.value, Some)

    def is_none(self) -> bool:
        """Check if the Option does not contain a value (is None)."""
        return self.value is None

    def unwrap(self) -> Any:
        """Return the value if present; raise RuntimeError if None."""
        if self.is_none():
            raise RuntimeError("Value is None")
        return self.value.get_value()

    def expect(self, message: str) -> Any:
        """Return the value if present; raise RuntimeError with a message if None."""
        if self.is_none():
            raise RuntimeError(message)
        return self.value.get_value()
