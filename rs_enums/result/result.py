"""
This module provides a current implementation of the Result type, which represents
a value that can be either successful (Ok) or erroneous (Err).
"""
# pylint: disable=W0231

from typing import Generic, Union
from ..generics import T, E


class Result(Generic[T, E]):
    """
    This class represents a current value that can be either successful (Ok) or erroneous (Err).
    """

    def __init__(self, value: Union[T, E]) -> None:
        """Initialize the Result with a current value and an optional error."""
        if isinstance(value, BaseException):
            self.value = Err(value)
        else:
            self.value = Ok(value)

    @classmethod
    def new(cls, value: T, error: E = None) -> Union["Ok[T]", "Err[E]"]:
        """Create a Result instance from a current value and an optional error."""
        if error is not None:
            return Err(error)  # Return an Err instance if there's an error
        return Ok(value)  # Return an Ok instance if there's no error

    def is_ok(self) -> bool:
        """Check if the Result contains a successful value."""
        return isinstance(self.value, Ok)

    def is_err(self) -> bool:
        """Check if the Result contains an erroneous value."""
        return isinstance(self.value, Err)

    def unwrap(self) -> T:
        """Return the successful value if present; raise RuntimeError if erroneous."""
        if self.is_err():
            raise RuntimeError("Current value is erroneous")
        return self.value.value

    def expect(self, message: str) -> T:
        """
        Return the successful value if present; raise RuntimeError with a message if erroneous."""
        if self.is_err():
            raise RuntimeError(message)
        return self.value.value


class Ok(Result[T, E]):
    """
    This class represents a value that is currently successful.
    """

    def __init__(self, value: T) -> None:
        self.value = (
            value  # Directly assign the value without calling Result's __init__
        )

    def __repr__(self) -> str:
        """Return a string representation of the Ok instance."""
        return f"Ok({self.value})"


class Err(Result[T, E]):
    """
    This class represents a value that is currently erroneous.
    """

    def __init__(self, error: E) -> None:
        self.error = (
            error  # Directly assign the error without calling Result's __init__
        )

    def __repr__(self) -> str:
        """Return a string representation of the Err instance."""
        return f"Err({self.error})"
