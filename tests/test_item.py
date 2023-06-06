"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture()
def cls_obj():
    return Item("Флешка", 500, 10)


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

