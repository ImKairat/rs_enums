# rs_enums

![Version](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ImKairat/rs_enums/gh-pages/version.json)
[![Pylint Status](https://github.com/ImKairat/rs_enums/actions/workflows/pylint.yml/badge.svg)](https://github.com/ImKairat/rs_enums/actions/workflows/pylint.yml)
[![Pytest Status](https://github.com/ImKairat/rs_enums/actions/workflows/pytest.yml/badge.svg)](https://github.com/ImKairat/rs_enums/actions/workflows/pytest.yml)
[![Contributing Guidelines](https://img.shields.io/badge/Contributing-Guidelines-blue)](CONTRIBUTING.md)

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

## Result and Option Types

### `Option`
The `Option` type represents an optional value that can either be present (`Some`) or absent (`None`). It provides methods to safely handle values that may not exist.

#### Features:
- **`Some`**: Represents a value that is present.
- **`is_some()`**: Checks if the value is present.
- **`is_none()`**: Checks if the value is absent.
- **`unwrap()`**: Returns the value if present; raises an error if absent.
- **`expect(message)`**: Returns the value if present; raises an error with a custom message if absent.

### `Result`
The `Result` type represents a value that can either be successful (`Ok`) or erroneous (`Err`). It is useful for handling operations that may succeed or fail.

#### Features:
- **`Ok`**: Represents a successful value.
- **`Err`**: Represents an error value.
- **`is_ok()`**: Checks if the result is successful.
- **`is_err()`**: Checks if the result is erroneous.
- **`unwrap()`**: Returns the successful value if present; raises an error if erroneous.
- **`expect(message)`**: Returns the successful value if present; raises an error with a custom message if erroneous.

## Usage Example

```python
from rs_enums.option import Option
from rs_enums.result import Result

# Example of Option
opt = Option(42)
if opt.is_some():
    print(opt.unwrap())  # Output: 42

# Example of Result
result = Result.new(value="Success")
if result.is_ok():
    print(result.unwrap())  # Output: Success
```

## License

This project is licensed under the [Apache-2.0 license](LICENSE).

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to contribute to this project.
