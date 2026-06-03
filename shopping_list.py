from ingredient import Ingredient 
from recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        new_recipe = recipe.scale(portions)
        for ing in new_recipe.ingredients:
            self._items.append((ing, recipe.title))
    
    def remove_recipe(self, title):
        new_items = []
        for ingredient, recipe_title in self._items:
            if recipe_title != title:
                new_items.append((ingredient, recipe_title))
        self._items = new_items

    def get_list(self):
        answer = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in answer:
                answer[key] += ingredient.quantity
            else:
                answer[key] = ingredient.quantity
        answer_list = []
        for (name, unit), quantity in answer.items():
            answer_list.append(Ingredient(name, quantity, unit))
        answer_list.sort(key=lambda x: x.name)
        return answer_list

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list
