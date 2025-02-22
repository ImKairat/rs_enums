import pytest
from option import Option


@pytest.fixture
def data() -> list[str]:
    return ["Some"]


class TestOption:
    def test_some(self):
        opt = Option(23)
        assert opt.is_some()
        assert not opt.is_none()
