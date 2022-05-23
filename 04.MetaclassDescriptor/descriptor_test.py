import pytest

from descriptor import Data


@pytest.mark.parametrize(
    "i,is_valid", [(1, True), (-1, True), (False, False), ("string", False)]
)
def test_int(i, is_valid):
    d = Data()
    try:
        d.num = i
        assert is_valid
    except AttributeError:
        assert not is_valid


@pytest.mark.parametrize(
    "i,is_valid", [(1, False), ("", True), (False, False), ("string", True)]
)
def test_str(i, is_valid):
    d = Data()
    try:
        d.name = i
        assert is_valid
    except AttributeError:
        assert not is_valid


@pytest.mark.parametrize(
    "i,is_valid", [(1, True), (-1, False), (False, False), ("string", False)]
)
def test_positive_int(i, is_valid):
    d = Data()
    try:
        d.price = i
        assert is_valid
    except AttributeError:
        assert not is_valid
