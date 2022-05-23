import pytest
from metaclass import CustomClass


def test_line():
    inst = CustomClass()
    try:
        inst.line()
        assert False
    except AttributeError:
        assert True
    assert inst.custom_line() == 100


@pytest.mark.parametrize("custom_class", [CustomClass, CustomClass()])
def test_x(custom_class):
    try:
        custom_class.x
        assert False
    except AttributeError:
        assert True
    assert custom_class.custom_x == 50


def test_str():
    inst = CustomClass()
    assert str(inst) == "Custom_by_metaclass"


def test_setattr():
    inst = CustomClass(val=5)
    assert inst.custom_val == 5
    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later"
