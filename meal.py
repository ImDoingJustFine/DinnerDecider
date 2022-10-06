from unicodedata import name
import json


class Meal:
    """Class that holds all necessary characteristics of a meal"""
    

    def __init__(self, name:str, protein:str, cost:int, difficulty:int):
        """Initialize name, protein type, cost, and difficulty to create the meal"""
        self.name = name.lower()
        self.protein = protein.lower()
        # TODO: validate range
        self.difficulty = difficulty
        self.cost = cost