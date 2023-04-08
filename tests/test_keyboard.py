from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def exp():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(exp):
    assert exp.language == "EN"
    assert str(exp) == "Dark Project KD87A"

def test_change_language(exp):
    exp.change_lang()
    assert str(exp.language) == "RU"
    exp.change_lang().change_lang()
    assert str(exp.language) == "RU"
    with pytest.raises(AttributeError):
        exp.language = "CH"