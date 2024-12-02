from typing import Any


class Some:
    """
    This class represents a value that is present and can be used safely.
    """
    def __init__(self, value: Any) -> None:
        self.value: Any = value
    

class Option(Some):
    """
    This class represents an optional value that can be either present (Some) 
    or absent (None).

    Args:
        Some (_type_): _description_
    """
    def __init__(self, value: Any | Some | None) -> None:
        """Initialize the Option with a value, which can be Some or None."""
        if type(value) == Some:
            super().__init__(value=value)
            
        elif value is None:
            self.value = None
            
        else:
            super().__init__(value=value)
        
    @classmethod
    def From(cls, value: Any | None) -> 'Option':
        """Create an Option instance from a value, returning None if the value is None."""
        return cls(Some(value) if value is not None else None)
    
    def is_some(self) -> bool:
        """Check if the Option contains a value (is not None)."""
        return self.value is not None
    
    def is_none(self) -> bool:
        """Check if the Option does not contain a value (is None)."""
        return self.value is None
        
    def unwrap(self) -> Any | None:
        """Return the value if present; raise RuntimeError if None."""
        match self.value:
            case None:
                raise RuntimeError        
            case _:
                return self.value
            
    def expect(self, message: str) -> Any | None:
        """Return the value if present; raise RuntimeError with a message if None."""
        match self.value:
            case None:
                raise RuntimeError(message)        
            case _:
                return self.value
            


__all__ = [
    "Some",
    "Option",
]