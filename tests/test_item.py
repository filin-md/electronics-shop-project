"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture()
def cls_obj():
    return Item("Флешка", 500, 10)

@pytest.fixture()
def phone_obj():
    return Phone("Siemens S65", 50000, 1, 1)


# def test_item_props():
#     assert csl_obj("Флешка", 500, 10).name == "Флешка"
#     assert csl_obj("Флешка", 500, 10).price == 500
#     assert csl_obj("Флешка", 500, 10).quantity == 10

def test_init(cls_obj):

    assert cls_obj.name == "Флешка"
    assert cls_obj.price == 500
    assert cls_obj.quantity == 10


def test_calculate_total_price(cls_obj):

    assert cls_obj.calculate_total_price() == 5000

def test_apply_discount(cls_obj):
    cls_obj.pay_rate = 0.8
    cls_obj.apply_discount()
    assert cls_obj.price == 400


def test_name_setter(cls_obj):
    cls_obj.name = "Пульт"
    assert cls_obj.name == "Пульт"

def test_instantiate_from_csv(cls_obj):
    cls_obj.instantiate_from_csv()
    assert cls_obj.all[0].name == "Смартфон"
    assert cls_obj.all[1].price == "1000"
    assert cls_obj.all[2].quantity == "5"

def test_string_to_number(cls_obj):
    assert cls_obj.string_to_number("1234") == 1234
    assert cls_obj.string_to_number("13.43") == 13

def test_repr(cls_obj):
    assert repr(cls_obj) == "Item('Флешка', 500, 10)"

def test_str(cls_obj):
    assert str(cls_obj) == "Флешка"


def test_add(cls_obj, phone_obj):
    assert cls_obj + phone_obj == 11
    with pytest.raises(AttributeError):
        phone_obj + 1
        cls_obj + "string"


def test_file_not_found(cls_obj):
    with pytest.raises(FileNotFoundError):
        cls_obj.instantiate_from_csv()

def test_invalid_csv(cls_obj):
    with pytest.raises(InstantiateCSVError):
        cls_obj.instantiate_from_csv()


