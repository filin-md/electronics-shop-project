import pytest

from src.phone import Phone


@pytest.fixture()
def phone_obj():
    return Phone("Siemens S65", 50000, 1, 1)

def test_init(phone_obj):

    assert phone_obj.name == "Siemens S65"
    assert phone_obj.price == 50000
    assert phone_obj.quantity == 1
    assert phone_obj.number_of_sim == 1

def test_repr(phone_obj):
    assert repr(phone_obj) == "Phone('Siemens S65', 50000, 1, 1)"
