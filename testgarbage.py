from meal import Meal
from mealdata import Meal_Data

burger = Meal("burgers", "ground", 2, 2)
taco = Meal("taco", "ground", 1, 2)

data = Meal_Data()

data.meal_add(taco)
# data.meal_add(burger)

# mealtest1 = data.meal_get()[0]

# print(mealtest1.name)
# print(mealtest1.protein)
# print(mealtest1.difficulty)
# print(mealtest1.cost)