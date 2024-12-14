"""
This module contains tests for the Result class from rs_enums.
"""
import os
import sys
import pytest   # type: ignore
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rs_enums import Result  # pylint: disable=C0413


class TestResult:
    """Test the behavior of the Result class with various types of input data."""

    def test_result_creation_with_various_inputs(self, generate_random_data):
        """Verify that the class correctly handles different types of input data."""
        for value in generate_random_data:
            result_instance = Result(value)
            if isinstance(value, BaseException):
                assert result_instance.is_err() is True
                with pytest.raises(RuntimeError) as exc_info:
                    result_instance.unwrap()
                assert str(exc_info.value) == "Current value is erroneous"
                with pytest.raises(RuntimeError) as exc_info:
                    result_instance.expect("Some error")
                assert str(exc_info.value) == "Some error"
            else:
                assert result_instance.is_ok() is True
                assert result_instance.unwrap() == value
                assert result_instance.expect("Some error") == value

    def test_result_with_different_types(self, generate_random_data):
        """Test with different types of values."""
        for value in generate_random_data:
            result_instance = Result(value)
            if isinstance(value, BaseException):
                assert result_instance.is_err() is True
                with pytest.raises(RuntimeError) as exc_info:
                    result_instance.unwrap()
                assert str(exc_info.value) == "Current value is erroneous"
                with pytest.raises(RuntimeError) as exc_info:
                    result_instance.expect("Some error")
                assert str(exc_info.value) == "Some error"
            else:
                assert result_instance.is_ok() is True
                assert result_instance.unwrap() == value
                assert result_instance.expect("Some error") == value
