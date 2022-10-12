from meal import Meal
from mealdata import Meal_Data
import json
import unittest

class TestCases(unittest.TestCase):
    """Testing file to verify function of the... well - functions relating to the Meal Class and associated data layer"""

    #>-----------------------------------------------------------<#
    #  Predefined objects of the Meal Class for testing purposes  #
    #>-----------------------------------------------------------<#


    filename = "foodinfo.json" # -----------------------------------------> Name of JSON file that data is supposed to save to
    addtest = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for "Single Add Test"
    addtest2 = Meal("steak", "beef", 5, 1) # -----------------------------> Meal Object for "Multiple Add Test"
    addtest2 = Meal("fried chicken sandwhich", "chicken", 2, 3) # --------> Meal Object for "Multiple Add Test"
    float = Meal("N/A", "N/A", 2.5, 3.1) # -------------------------------> Meal Object for "Float to Integer Test"
    above_bound = Meal("N/A", "N/A", 10, 10) # ---------------------------> Meal Object for "Above Bounds Test (Both for Difficulty and Cost)"
    below_bound = Meal("N/A", "N/A", -10, -10) # -------------------------> Meal Object for "Below Bounds Test (Both for Difficulty and Cost)"
    data = Meal_Data() # -------------------------------------------------> Instance of the data layer


    def clean_slate_test(self):
        """Erases all data in foodinfo.json for testing"""
        
        jsondata = ""
        
        with open(self.filename, 'w') as f:
            json.dump(jsondata, f)
    
    
    def single_add_test(self, meal:Meal):
        """Tests adding a single instance of the Meal class to foodinfo.json"""
        
        if meal == self.data.meal_add(self.addtest):
            print(f"Object saved to '{self.filename}' successfully")
        else:
            print(f"Object did not successfully save to '{self.filename}'")
        
        
    def multiple_add_test(self):
        """Tests adding multiple instances of the Meal Class to foodinfo.json"""
        
        
    def float_test(self):
        """Makes sure that floats are rounded and converted into integers"""
        
test = TestCases()

test.clean_slate_test()