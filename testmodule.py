from meal import Meal
from mealdata import Meal_Data
import json
import unittest

class TestCases(unittest.TestCase):
    """Testing file to verify function of the... well - functions relating to the Meal Class and associated data layer"""
    
        #>-------------------------------------------------------------------------<#
        #  Predefined variables and instance(s) for use within the TestCases class  #
        #>-------------------------------------------------------------------------<#

    filename = "foodinfo.json" # -------------------------------------> Name of JSON file that data is supposed to save to
    data = Meal_Data() # ---------------------------------------------> Instance of the data layer
    emptylist = [] # -------------------------------------------------------> Empty List for Clean Slate Test

    # Works as intended
    def clean_slate(self):
        """Erases all data in foodinfo.json for testing"""
        
        with open(self.filename, 'w') as f:
            json.dump([], f)
            
    
    # Works as intended        
    def test_clean_slate(self):
        """There should be no items in the list"""

        meal1 = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for Clean Slate Test (Goal: Add then Remove)
        meal2 = Meal("fried chicken sandwhich", "chicken", 2, 3) # ---------> Meal Object for Clean Slate Test (Goal: Add then Remove)
        meal3 = Meal("steak", "beef", 5, 1) # ------------------------------> Meal Object for Clean Slate Test (Goal: Add then Remove)
        
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
        self.data.meal_add(meal1)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 1)
        self.data.meal_add(meal2)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 2)
        self.data.meal_add(meal3)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 3)
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
        
    
    # Works as intended        
    def test_single_add(self):
        """Ability to write multiple  a single instance of the Meal class to foodinfo.json"""
        
        meal = Meal("taco", "ground", 1, 2) # ------------------------------------> Meal Object for Single Add Test (Goal: Add)
        
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
        self.data.meal_add(meal)
        meal_gets = self.data.meal_get()
        self.assertEqual(meal_gets[0].name, meal.name)
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
    
    # Does not work as intended
    # -- With all following test functions and lines 81 and 82 commented out, there should be instances of the Meal class stored in a list inside foodinfo.json
    # -- Instead, we are left with an empty list though the code supposedly passes all tests
    def test_multiple_add(self):
        """Ability to write multiple instances of the Meal class to foodinfo.json"""

        meal0 = Meal("fried chicken sandwhich", "chicken", 2, 3) # --------------> Meal Object for Multiple Add Test (Goal: Add)
        meal1 = Meal("steak", "beef", 5, 1) # -----------------------------------> Meal Object for Multiple Add Test (Goal: Add)
        
        self.clean_slate() # -- >> Overwrites whatever's in foodinfo.json to an empty list
        self.assertEqual(self.data.meal_get(), self.emptylist) # -- >> Makes sure self.clean_slate() did its job
        self.data.meal_add(meal0) # ------------ \
        meal_gets = self.data.meal_get() # ----- >> Adds meal0 (fried chicken sandwich) to foodinfo.json and checks that there is only one item in the list
        self.assertEqual(len(meal_gets), 1) # -- /
        self.data.meal_add(meal1) # ------------ \
        meal_gets = self.data.meal_get() # ----- >> Adds meal1 (steak) to foodinfo.json and checks that there are two items in the list
        self.assertEqual(len(meal_gets), 2) # -- /
        self.assertEqual(meal_gets[0].name, meal0.name) # -- >> Checks that the first meal from foodinfo.json is meal0 (fried chicken sandwhich)
        self.assertEqual(meal_gets[1].name, meal1.name) # -- >> Checks that the second meal from foodinfo.json is meal1 (steak)
        self.clean_slate() # -- >> Overwrites whatever's in foodinfo.json to an empty list
        self.assertEqual(self.data.meal_get(), self.emptylist) # -- >> Makes sure self.clean_slate() did its job
     
    
    # Works as intended
    def test_float(self):
        """Floats are rounded and converted into integers"""
        
        float = Meal("N/A", "N/A", 2.51, 2.51) # -------------------------------> Meal Object for Float to Integer Test (Goal: Round Values Up to an Integer)
        
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
        self.assertEqual(float.cost, 3)
        self.assertEqual(float.difficulty, 3)
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
    
    
    # Works as inteded
    def test_def_limit(self):
        """Cost and Difficulty values are between 1 and 5"""
        
        above_bound = Meal("N/A", "N/A", 10, 10) # -----------------------------> Meal Object for Above Bounds Test (Both for Difficulty and Cost) (Goal: Correct to 5)
        below_bound = Meal("N/A", "N/A", -10, -10) # ---------------------------> Meal Object for Below Bounds Test (Both for Difficulty and Cost) (Goal: Correct to 1)
        
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
        self.assertEqual(above_bound.cost, 5)
        self.assertEqual(above_bound.difficulty, 5)
        self.assertEqual(below_bound.cost, 1)
        self.assertEqual(below_bound.difficulty, 1)
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
       
    # Works as intended    
    def test_single_delete(self):
        """Taco meal should be removed from the list"""
        
        meal1 = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for Single Delete Test (Goal: Add then Remove)
        meal2 = Meal("fried chicken sandwhich", "chicken", 2, 3) # ---------> Meal Object for Single Delete Test (Goal: Add)
        meal3 = Meal("steak", "beef", 5, 1) # ------------------------------> Meal Object for Single Delete Test (Goal: Add)
        
        self.clean_slate()
        self.assertEqual(self.data.meal_get(), self.emptylist)
        self.data.meal_add(meal1)
        self.data.meal_add(meal2)
        self.data.meal_add(meal3)
        meal_gets = self.data.meal_get()
        # self.assertEqual()
        self.assertEqual(meal_gets[0].name, meal1.name)
        self.assertEqual(meal_gets[1].name, meal2.name)
        self.assertEqual(meal_gets[2].name, meal3.name)
        self.data.meal_del(meal1.name)
        meal_gets = self.data.meal_get()
        self.assertEqual(meal_gets[0].name, meal2.name)
        self.assertEqual(meal_gets[1].name, meal3.name)   
        # self.clean_slate() # -- >> Overwrites whatever's in foodinfo.json to an empty list
        # self.assertEqual(self.data.meal_get(), self.emptylist) # -- >> Makes sure self.clean_slate() did its job
    
    
    # Does not work as intended
    # -- With lines 137, 138, 172, and 173 commented out, there should be one instance of the Meal class in a list inside foodinfo.json
    # -- Instead foodinfo.json contains a list with two instances of the meal class in a list inside foodinfo.json
    # -- Somehow, the code supposedly passes all tests
    def test_multiple_delete(self):
        """Taco and Fried Chicken Sandwhich should be removed from the list"""
        
        meal1 = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for Single Delete Test (Goal: Add then Remove)
        meal2 = Meal("fried chicken sandwhich", "chicken", 2, 3) # ---------> Meal Object for Single Delete Test (Goal: Add then Remove)
        meal3 = Meal("steak", "beef", 5, 1) # ------------------------------> Meal Object for Single Delete Test (Goal: Add)
        
        self.clean_slate() # -- >> Overwrites whatever's in foodinfo.json to an empty list
        self.assertEqual(self.data.meal_get(), self.emptylist) # -- >> Makes sure self.clean_slate() did its job
        self.data.meal_add(meal1) # ------------ \
        meal_gets = self.data.meal_get() # ----- >> Adds meal1 (taco) to foodinfo.json and checks that there is only one item in the list
        self.assertEqual(len(meal_gets), 1) # -- /
        self.data.meal_add(meal2) # ------------ \
        meal_gets = self.data.meal_get() # ----- >> Adds meal2 (fried chicken sandwich) to foodinfo.json and checks that there are two items in the list
        self.assertEqual(len(meal_gets), 2) # -- /
        self.data.meal_add(meal3) # ------------ \
        meal_gets = self.data.meal_get() # ----- >> Adds meal3 (steak) to foodinfo.json and checks that there are three items in the list
        self.assertEqual(len(meal_gets), 3) # -- /
        meal_gets = self.data.meal_get() # >> Gets the full list of meals
        self.assertEqual(meal_gets[0].name, meal1.name) # -- \
        self.assertEqual(meal_gets[1].name, meal2.name) # -- >> Ensures all meals are in the expected order
        self.assertEqual(meal_gets[2].name, meal3.name) # -- /
        self.data.meal_del(meal1.name) # -- \
        self.data.meal_del(meal2.name) # -- >> Removes meal1 (taco) and meal2 (fried chicked sandwich) from the list and saves modified list to foodinfo.json
        meal_gets = self.data.meal_get() # ----- \
        self.assertEqual(len(meal_gets), 1) # -- >> Ensures there is only one remaining item in the list
        self.assertEqual(meal_gets[0].name, meal3.name) # -- >> Ensures the remaining item is meal3 (steak)
    #     # self.clean_slate() # -- >> Overwrites whatever's in foodinfo.json to an empty list
    #     # self.assertEqual(self.data.meal_get(), self.emptylist) # -- >> Makes sure self.clean_slate() did its job
  
if __name__ == '__main__':
    unittest.main()