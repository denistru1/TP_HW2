import pytest
from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList

def test_ingredient_init():
    a = Ingredient("Мука", 500, "г")
    assert a.name == "Мука"
    assert a.quantity == 500
    assert a.unit == "г"


def test_ingredient_str():
    a = Ingredient("Мука", 500, "г")
    assert str(a) == "Мука: 500.0 г"


def test_eq_same_name_unit_different_quantity():
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 100, "г")
    assert a == b

def test_eq_different_name():
    a = Ingredient("Сахар", 10, "г")
    b = Ingredient("Соль", 10, "г")
    assert a != b

def test__eq_different_unit():
    a = Ingredient("Сахар", 10, "г")
    b = Ingredient("Сахар", 10, "кг")
    assert a != b


def test_recipe_init():
    r = Recipe("Салат")
    assert r.title == "Салат"
    assert r.ingredients == []


def test_add_new_ingredient():
    r = Recipe("Салат")
    i = Ingredient("Помидоры", 500, "г")
    r.add_ingredient(i)
    assert len(r.ingredients) == 1
    assert r.ingredients[0].name == "Помидоры"
    assert r.ingredients[0].quantity == 500


def test_add_ingredient_same_name():
    r = Recipe("Салат")
    i1 = Ingredient("Помидоры", 500, "г")
    i2 = Ingredient("Помидоры", 100, "г")
    r.add_ingredient(i1)
    r.add_ingredient(i2)
    assert len(r.ingredients) == 1
    assert r.ingredients[0].quantity == 600

def test_scale_new_recipe():
    r = Recipe("Салат")
    i = Ingredient("Помидоры", 500, "г")
    r.add_ingredient(i)
    r2 = Recipe("Салат")
    i2 = Ingredient("Помидоры", 600, "г")
    assert r2 is not r
    assert r2.title == "Салат"
    assert r.ingredients[0].quantity == 500


def test_scale_quantity():
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    r.add_ingredient(Ingredient("Огурцы", 300, "г"))
    r2 = r.scale(2)
    assert r2.ingredients[0].quantity == 1000
    assert r2.ingredients[1].quantity == 600

def test_invalid_ratio():
    r = Recipe("Салат")
    with pytest.raises(ValueError):
        r.scale(0)

def test_len_recipe():
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    r.add_ingredient(Ingredient("Помидоры", 200, "г"))
    r.add_ingredient(Ingredient("Огруцы", 300, "г"))
    assert len(r) == 2

