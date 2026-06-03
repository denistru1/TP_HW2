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

def test_add_recipe():
    l = ShoppingList()
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    l.add_recipe(r, 2)
    assert len(l._items) > 0

def test_add_recipe_invalid_portions():
    l = ShoppingList()
    r = Recipe("Салат")
    with pytest.raises(ValueError):
        l.add_recipe(r, 0)


def test_remove_recipe():
    l = ShoppingList()
    r1 = Recipe("Салат")
    r1.add_ingredient(Ingredient("Помидоры", 500, "г"))
    r2 = Recipe("Торт")
    r2.add_ingredient(Ingredient("Мука", 1000, "г"))
    l.add_recipe(r1, 1)
    l.add_recipe(r2, 1)
    l.remove_recipe("Салат")
    for ing, title in l._items:
        assert title != "Салат"


def test_remove_recipe_not_exists():
    l = ShoppingList()
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    l.add_recipe(r, 1)
    l.remove_recipe("Торт")
    assert len(l._items) > 0


def test_get_list_sum_same_ingredients():
    l = ShoppingList()
    r1 = Recipe("Торт")
    r1.add_ingredient(Ingredient("Сахар", 200, "г"))
    r2 = Recipe("Пирог")
    r2.add_ingredient(Ingredient("Сахар", 200, "г"))
    l.add_recipe(r1, 1)
    l.add_recipe(r2, 1)
    result = l.get_list()
    assert len(result) == 1
    assert result[0].quantity == 400


def test_get_list_sorted():
    l = ShoppingList()
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    r.add_ingredient(Ingredient("Огурцы", 300, "г"))
    l.add_recipe(r, 1)
    result = l.get_list()
    sp = []
    for i in result:
        sp.append(i.name)
    assert sp == sorted(sp)


def test_add_combines_lists():
    l1 = ShoppingList()
    l2 = ShoppingList()
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    l1.add_recipe(r, 1)
    l2.add_recipe(r, 1)
    l3 = l1 + l2
    assert l3 is not l1
    assert l3 is not l2
    assert len(l3._items) == len(l1._items) + len(l2._items)


def test_add_doesnt_change_original():
    l1 = ShoppingList()
    l2 = ShoppingList()
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Помидоры", 500, "г"))
    l1.add_recipe(r, 1)
    l2.add_recipe(r, 1)
    l1_len = len(l1._items)
    l2_len = len(l2._items)
    l3 = l1 + l2
    assert len(l1._items) == l1_len
    assert len(l2._items) == l2_len

