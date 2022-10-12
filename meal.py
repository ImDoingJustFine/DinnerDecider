import json

class Meal:
    """Class that holds all necessary characteristics of a meal"""
    
    def __init__(self, name:str, protein:str, cost:int, difficulty:int):
        """Initialize name, protein type, cost, and difficulty to create the meal"""
        
        self.name = name.lower()
        self.protein = protein.lower()
        # TODO: validate range
        self.cost = self.validate_cost(cost)
        self.difficulty = self.validate_difficulty(difficulty)
        
    def as_dict(self):
        """Turns an instance of the Meal object into a dictionary"""
        
        meal_dict = {'name':self.name, 'protein':self.protein, 'cost':self.cost, 'difficulty':self.difficulty}
        return meal_dict
    
    def validate_cost(self, cost):
        """Validates that cost is within boundries and has no decimal places"""
        
        if cost > 5:
            cost = 5
        if cost < 1:
            cost = 1
        if isinstance(cost) == False:
            int(round(cost))
        return self.cost
    
    def validate_difficulty(self, difficulty):
        """Validates that difficulty is within boundries and has no decimal places"""
        
        if difficulty > 5:
            difficulty = 5
        if difficulty < 1:
            difficulty = 1
        if isinstance(difficulty) == False:
            int(round(difficulty))
        return difficulty