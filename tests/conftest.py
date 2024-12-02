import pytest  # type: ignore
import random


@pytest.fixture
def generate_random_data():
    """Generate list from 1000 random data of various types."""
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
    
    for i in range(1000):
        result.append(random.choice(data_types))
    
    return result