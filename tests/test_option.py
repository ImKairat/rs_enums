"""
This module contains tests for the Option class from rs_enums.
"""
import os
import sys
import pytest_lazyfixture   # type: ignore
from rs_enums import Option
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_new(generate_random_data):
    """
    This test checks the behavior of the Option class with various types of input data.
    It verifies that the class correctly handles None values and unwraps the expected values.
    
    Args:
        generate_random_data (_type_): _description_
    """
    for i in generate_random_data:
        x = Option(i)
        if i is None:
            with pytest_lazyfixture.raises(RuntimeError) as exc_info:
                x.expect("Some error")
                assert str(exc_info.value) == "Some error"
            with pytest_lazyfixture.raises(RuntimeError) as exc_info:
                x.unwrap()
                assert str(exc_info.value) == ""
        else:
            assert x.expect("Some error") == i
            assert x.unwrap() == i
        assert x.is_none() == (i is None)
        assert x.is_some() == (i is not None)
        