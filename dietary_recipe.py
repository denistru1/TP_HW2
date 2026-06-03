from ingredient import Ingredient 
from recipe import Recipe
from shopping_list import ShoppingList

class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title)
        self.diet_type = diet_type
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
    
    def scale(self, ratio):
        scaled = super().scale(ratio)
        new_recipe = DietaryRecipe(self.title, self.diet_type)
        new_recipe.ingredients = scaled.ingredients
        return new_recipe

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"