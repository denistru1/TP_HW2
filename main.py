from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList
from dietary_recipe import DietaryRecipe

tomatos = Ingredient("Помидоры", 500, "г")
cucumbers = Ingredient("Огурцы", 200, "г")
onion = Ingredient("Лук", 1, "шт")
oil = Ingredient("Масло", 30, "мл")

# Создаем рецепт
vegetable_salad = Recipe("Овощной салат")
# добавляем ингредиенты
vegetable_salad.add_ingredient(tomatos)
vegetable_salad.add_ingredient(cucumbers)
vegetable_salad.add_ingredient(onion)
vegetable_salad.add_ingredient(oil)
print(vegetable_salad)

# Увеличиваем количество до двух порций
scaled_salad = vegetable_salad.scale(2)
print(scaled_salad)

# Создаем список покупок
sl = ShoppingList()
sl.add_recipe(vegetable_salad, 2)
for i in sl.get_list():
    print(f"  - {i}")

# Диетический рецепт
salad = DietaryRecipe("вегетарианский салат", "вегетарианский", [tomatos, cucumbers])
print(f"\n{salad}")