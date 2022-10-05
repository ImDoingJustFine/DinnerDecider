from random import choice
from meal import Meal

mealtest1 = Meal("burgers", "ground", 2, 2)
mealtest2 = Meal("steak", "beef", 1, 5)
mealtest3 = Meal("pork chop", "pork", 1, 2)

meallist = [mealtest1, mealtest2, mealtest3]

print(mealtest1.tostring())

print(mealtest1.meal_name())
print(mealtest1.protein_type())
print(mealtest1.difficulty_rating())
print(mealtest1.cost_rating())