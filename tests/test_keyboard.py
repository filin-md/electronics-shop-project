import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard_obj():
    return Keyboard("MSI GK30", 3500, 1)

def test_init(keyboard_obj):

    assert keyboard_obj.name == "MSI GK30"
    assert keyboard_obj.price == 3500
    assert keyboard_obj.quantity == 1
    assert keyboard_obj.language == "EN"

def test_change_lang(keyboard_obj):
    keyboard_obj.change_lang()
    assert keyboard_obj.language == "RU"
    keyboard_obj.change_lang()
    assert keyboard_obj.language == "EN"
