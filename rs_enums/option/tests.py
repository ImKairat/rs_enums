import pytest
from typing import Any
from .option import Option, Some


@pytest.fixture
def data() -> list[Any]:
    xdata = [
        "Some",
        12,
        32.5,
        True,
        [1, 2, 3],
        {"key": "value"},
        None,
    ]
    return xdata


class TestSome:
    def test_get_value(self, data):
        for d in data:
            some = Some(d)
            assert some.get_value() == d

    def test_is_present(self, data):
        for d in data:
            some = Some(d)
            if d is None:
                assert not some.is_present()
            else:
                assert some.is_present()


class TestOption:
    def test_new(self, data: list[Any]):
        for d in data:
            option = Option.new(d)
            if d is not None:
                assert option.is_some()
            else:
                assert option.is_none()

    def test_unwrap(self, data: list[Any]):
        for d in data:
            option = Option.new(d)
            if d is not None:
                assert option.unwrap() == d
            else:
                with pytest.raises(RuntimeError):
                    option.unwrap()
