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
        """Returns attributes of meal inquired based on name"""

        meal_desc = f"\n{self.name.title()} include(s) the following properties:\
            \nProtein:     -{self.protein.title()}-\
            \nDifficulty:  -{self.difficulty}-\
            \nCost Level:  -{self.cost}-"
        return meal_desc


mealtest1 = Meal("burgers", "ground", 1, 2)
print(mealtest1.tostring())