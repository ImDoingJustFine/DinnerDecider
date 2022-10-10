from unicodedata import name
import json


class Meal:
    """Class that holds all necessary characteristics of a meal"""
    
    def __init__(self, name:str, protein:str, cost:int, difficulty:int):
        """Initialize name, protein type, cost, and difficulty to create the meal"""
        
        self.name = name.lower()
        self.protein = protein.lower()
        # TODO: validate range
        self.cost = cost
        self.difficulty = difficulty
        
    def as_dict(self):
        """Turns an instance of the Meal object into a dictionary"""
        
        meal_dict = {'name':self.name, 'protein':self.protein, 'cost':self.cost, 'difficulty':self.difficulty}
        return meal_dict
    
    # def __init__(self, input:dict):
    #     """Initializes a meal from a Dictionary Input"""
        
    #     self.name = input['name']
    #     self.protein = input['protein']
    #     self.difficulty = input['difficulty']
    #     self.cost = input['cost']          