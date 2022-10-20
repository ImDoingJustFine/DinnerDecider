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
        # TODO: add a variable for time since last cooked
        
    def as_dict(self):
        """Turns an instance of the Meal object into a dictionary"""
        
        meal_dict = {'name':self.name, 'protein':self.protein, 'cost':self.cost, 'difficulty':self.difficulty}
        return meal_dict
    
    def validate_cost(self, cost):
        """Validates that cost is within boundries and has no decimal places"""
        
        if cost > 5:
            adjusted_cost = 5
            return round(adjusted_cost)
        else: pass
        if cost < 1:
            adjusted_cost = 1
            return round(adjusted_cost)
        else:
            return round(cost)
    
    def validate_difficulty(self, difficulty):
        """Validates that difficulty is within boundries and has no decimal places"""
        
        if difficulty > 5:
            adjusted_difficulty = 5
            return round(adjusted_difficulty)
        else: pass
        if difficulty < 1:
            adjusted_difficulty = 1
            return round(adjusted_difficulty)
        else:
            return round(difficulty)