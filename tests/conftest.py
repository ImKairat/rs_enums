"""
This module contains fixtures for testing the Option class from rs_enums.
"""
import random
import pytest   # type: ignore


@pytest.fixture
def generate_random_data() -> list:
    """Generate a list of 1000 random data of various types."""
    data_types = [
        lambda: random.randint(1, 100),
        lambda: random.uniform(1.0, 100.0),
        lambda: random.choice(["a", "b", "c"]),
        lambda: [random.randint(1, 10) for _ in range(3)],
        lambda: {"key": random.randint(1, 10)},
        lambda: bool(random.getrandbits(1)),
        lambda: None
    ]
    result = []
    for _ in range(1000):
        result.append(random.choice(data_types)())
    return result
