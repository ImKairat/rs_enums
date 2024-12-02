# rs_enums

`rs_enums` is a Python module inspired by Rust’s `Option` and `Result` enums. It provides functional programming constructs for handling optional values (`Option`) and results (`Result`) with success or error outcomes. This module enables safer and more expressive code by allowing you to work with values that may or may not exist, or operations that may succeed or fail. 
### Features include:
- **`Option`**: Represents a value that may or may not be present (`Some` or `None`).
- **`Result`**: Represents an operation that can either succeed (`Ok`) or fail (`Err`).
- Common methods like `is_some()`, `is_none()`, `is_ok()`, and `is_err()` are included for easy handling of these types.

## Installation

Install via `pip`:

```bash
pip install rs_enums
```

## Usage Example

```python
from rs_enums import Optional, Result

# Example of Optional
opt = Optional(42)
if opt.is_some():
    print(opt.unwrap())  # Output: 42

# Example of Result
result = Result(value="Success")
if result.is_ok():
    print(result.unwrap())  # Output: Success
```

## License

This project is licensed under the [MIT License](LICENSE).
