from src.item import Item
from src.phone import Phone

import pytest


@pytest.fixture()
def expl1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(expl1):
    assert expl1.name == "iPhone 14"
    assert expl1.price == 120_000
    assert expl1.quantity == 5
    assert expl1.number_of_sim == 2


def test_phone_str(expl1):
    assert str(expl1) == 'iPhone 14'


def test_phone_repr(expl1):
    assert repr(expl1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_add(expl1):
    assert expl1 + expl1 == 10


def test_phone_radd(expl1):
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + expl1 == 25
    with pytest.raises(TypeError):
        item1 + int(56)

    with pytest.raises(TypeError):
         int(56) + expl1


def test_phone_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 3
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


