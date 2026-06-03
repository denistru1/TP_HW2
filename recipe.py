from ingredient import Ingredient

class Recipe:
    def __init__(self, title):
        self.title = title
        self.ingredients = []

    def add_ingredient(self, ingredient):
        for ing in self.ingredients:
            if ing == ingredient:
                int.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)):
            if ratio > 0:
                return True
        return False

    def scale(self, ratio):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Некорректный коэффициент")
        new_recipe = Recipe(self.title)
        for ing in self.ingredients:
            new_ingredient = Ingredient(
                ing.name,
                ing.quantity * ratio,
                ing.unit
            )
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe
            
    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        answer = self.title + "\n"
        for ing in self.ingredients:
            result += str(ing) + "\n"
        return answer