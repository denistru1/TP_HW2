import pytest
from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList

def test_ingredient_init():
    a = Ingredient("Мука", 500, "г")
    assert a.name == "Мука"
    assert a.quantity == 500
    assert a.unit == "г"

