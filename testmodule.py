from meal import Meal
from mealdata import Meal_Data
import json
import unittest

above_bound = Meal("N/A", "N/A", 10, 10) # ---------------------------> Meal Object for "Above Bounds Test (Both for Difficulty and Cost)"
below_bound = Meal("N/A", "N/A", -10, -10) # -------------------------> Meal Object for "Below Bounds Test (Both for Difficulty and Cost)"

class TestCases(unittest.TestCase):
    """Testing file to verify function of the... well - functions relating to the Meal Class and associated data layer"""
    
        #>-------------------------------------------------------------------------<#
        #  Predefined variables and instance(s) for use within the TestCases class  #
        #>-------------------------------------------------------------------------<#

    filename = "foodinfo.json" # -------------------------------------> Name of JSON file that data is supposed to save to
    data = Meal_Data() # ---------------------------------------------> Instance of the data layer


    def clean_slate_test(self):
        """Erases all data in foodinfo.json for testing"""
        
        with open(self.filename, 'w') as f:
            json.dump([], f)
    
    
    def test_single_add(self):
        """Ability to write multiple  a single instance of the Meal class to foodinfo.json"""
        
        meal = Meal("taco", "ground", 1, 2) # ------------------------------------> Meal Object for "Single Add Test"
        
        self.clean_slate_test()
        self.data.meal_add(meal)
        mealget = self.data.meal_get()
        self.assertEqual(mealget[0].name, meal.name)
    
    
    def test_multiple_add(self):
        """Ability to write multiple instances of the Meal class to foodinfo.json"""

        meal0 = Meal("fried chicken sandwhich", "chicken", 2, 3) # --------------> Meal Object for "Multiple Add Test"
        meal1 = Meal("steak", "beef", 5, 1) # -----------------------------------> Meal Object for "Multiple Add Test"
        
        self.clean_slate_test()
        self.data.meal_add(meal0)
        mealget0 = self.data.meal_get()
        self.data.meal_add(meal1)
        mealget1 = self.data.meal_get()    
        self.assertEqual(mealget0[0].name, meal0.name)
        self.assertEqual(mealget1[1].name, meal1.name)
        
    def test_float(self):
        """Floats are rounded and converted into integers"""
        
        float = Meal("N/A", "N/A", 2.51, 2.51) # -------------------------------> Meal Object for "Float to Integer Test"
        
        self.clean_slate_test()
        self.assertEqual(float.cost, 3)
        self.assertEqual(float.difficulty, 3)
    
    def test_def_limit(self):
        """Cost and Difficulty values are between 1 and 5"""
        
        above_bound = Meal("N/A", "N/A", 10, 10) # -----------------------------> Meal Object for "Above Bounds Test (Both for Difficulty and Cost)"
        below_bound = Meal("N/A", "N/A", -10, -10) # ---------------------------> Meal Object for "Below Bounds Test (Both for Difficulty and Cost)"
        
        self.clean_slate_test()
        self.assertEqual(above_bound.cost, 5)
        self.assertEqual(above_bound.difficulty, 5)
        self.assertEqual(below_bound.cost, 1)
        self.assertEqual(above_bound.difficulty, 1)
        
  
if __name__ == '__main__':
    unittest.main()