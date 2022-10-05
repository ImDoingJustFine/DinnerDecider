from unicodedata import name


class Meal:
    """Class that holds all necessary characteristics of a meal"""

    def __init__(self, name:str, protein:str, cost:int, difficulty:int):
        """Initialize name, protein type, cost, and difficulty to create the meal"""
        self.name = name.lower()
        self.protein = protein.lower()
        # TODO: validate range
        self.difficulty = difficulty
        self.cost = cost
        
    def tostring(self):
        """Returns string describing attributes of the meal"""

        meal_desc = f"\n{self.name.title()} include(s) the following properties:\
            \nProtein:     -{self.protein.title()}-\
            \nDifficulty:  -{self.difficulty}-\
            \nCost Level:  -{self.cost}-"
        return meal_desc

    def meal_name(self):
        """Returns the name of the meal"""

        return self.name

    def protein_type(self):
        """Returns the protein for the meal"""

        return self.protein

    def difficulty_rating(self):
        """Returns the difficulty rating of the meal"""

        return self.difficulty

    def cost_rating(self):
        """Returns the cost rating of the meal"""

        return self.cost


mealtest1 = Meal("burgers", "ground", 2, 2)
print(mealtest1.tostring())

print(mealtest1.meal_name())
print(mealtest1.protein_type())
print(mealtest1.difficulty_rating())
print(mealtest1.cost_rating())