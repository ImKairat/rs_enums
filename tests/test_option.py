"""
This module contains tests for the Option class from rs_enums.
"""
import os
import sys
import pytest   # type: ignore
from rs_enums import Option
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestOption:
    """Test the behavior of the Option class with various types of input data."""

    def test_option_creation_with_various_inputs(self, generate_random_data):
        """Verify that the class correctly handles None values and unwraps the expected values."""
        for value in generate_random_data:
            option_instance = Option(value)
            if value is None:
                with pytest.raises(RuntimeError) as exc_info:
                    option_instance.expect("Some error")
                assert str(exc_info.value) == "Some error"
                with pytest.raises(RuntimeError) as exc_info:
                    option_instance.unwrap()
                assert str(exc_info.value) == "Value is None"
            else:
                assert option_instance.expect("Some error") == value
                assert option_instance.unwrap() == value
                assert option_instance.is_none() == (value is None)
                assert option_instance.is_some() == (value is not None)

    def test_option_with_different_types(self, generate_random_data):
        """Test with different types of values."""
        for value in generate_random_data:
            option_instance = Option(value)
            assert option_instance.is_some() == (value is not None)
            if value is None:
                with pytest.raises(RuntimeError) as exc_info:
                    option_instance.unwrap()
                assert str(exc_info.value) == "Value is None"
                with pytest.raises(RuntimeError) as exc_info:
                    option_instance.expect("Should not be None")
                assert str(exc_info.value) == "Should not be None"
            else:
                assert option_instance.unwrap() == value
                assert option_instance.expect("Should not be None") == value

    def test_option_with_large_number(self):
        """Test with a large number."""
        large_number = 10**18
        option_instance = Option(large_number)
        assert option_instance.is_some() is True
        assert option_instance.unwrap() == large_number
        assert option_instance.expect("Should not be None") == large_number

    def test_option_with_custom_object(self):
        """Test with a custom object."""
        class CustomObject:
            """
            This class represents a custom object used for testing the Option class.
            It contains a name attribute and implements equality comparison.
            """
            def __init__(self, name):
                self.name = name

            def __eq__(self, other):
                return isinstance(other, CustomObject) and self.name == other.name

            def __str__(self):
                return f"CustomObject(name={self.name})"

        custom_obj = CustomObject("test")
        option_instance = Option(custom_obj)
        assert option_instance.is_some() is True
        assert option_instance.unwrap() == custom_obj
        assert option_instance.expect("Should not be None") == custom_obj
