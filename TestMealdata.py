from meal import Meal
from mealdata import Meal_Data
import json
import unittest

class TestMealdata(unittest.TestCase):
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
        f = open(self.filename, 'w')
        json.dump([], f)
        f.flush()
        f.close()


    # Works as intended
    def setUp(self):
        """Call before every test case."""
        print("setUp")
        self.clean_slate()


    # Works as intended
    def tearDown(self):
        """Call after every test case."""
        print("tearDown")
        # -- Code is only obiously broken if the line below is commented out
        # self.clean_slate()


    # Works as intended        
    def test_clean_slate(self):
        """There should be no items in the list"""

        meal1 = Meal("taco", "ground", 1, 2) # -----------------------------------> Meal Object for Clean Slate Test (Goal: Add then Remove)
        meal2 = Meal("fried chicken sandwich", "chicken", 2, 3) # ----------------------------------> Meal Object for Clean Slate Test (Goal: Add then Remove)
        meal3 = Meal("steak", "beef", 5, 1) # -------------------------------------> Meal Object for Clean Slate Test (Goal: Add then Remove)
        
        # -- Makes sure setUp() did its job
        self.assertEqual(self.data.meal_get(), self.emptylist)
        
        # -- Adds one meal (taco) and ensures that it is the only thing in the list
        self.data.meal_add(meal1)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 1)
        
        # -- Adds another meal (fried chicken sandwich) and ensures that it is the only thing in the list
        self.data.meal_add(meal2)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 2)

        # -- Manually wipes foodinfo.json and converts the contents to an empty list
        self.clean_slate()
        
        # -- Opens foodinfo.json, flushes the Python cache, loads foodinfo.json, and then closes foodinfo.json
        f = open(self.filename, 'r')
        f.flush()
        currentjson = json.load(f)
        f.close()
        
        # -- Confirms that wiping foodinfo.json with self.clean_slate() actually wiped the file
        self.assertEqual(currentjson, self.emptylist)
        meal_gets = self.data.meal_get()

        # -- Finally adds a single meal (steak) and ensures that is is the only item in the list after the wipe process
        self.data.meal_add(meal3)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 1)
        
    
    # Works as intended        
    def test_single_add(self):
        """Ability to write multiple a single instance of the Meal class to foodinfo.json"""
        
        meal = Meal("taco", "ground", 1, 2) # -----------------------------------> Meal Object for Single Add Test (Goal: Add)
        
        # -- Verify setup provides empty list
        self.assertEqual(self.data.meal_get(), self.emptylist)

        # -- Add meal and check return of meal_get
        self.data.meal_add(meal)
        meal_gets = self.data.meal_get()
        self.assertEqual(meal_gets[0].name, meal.name)
        
    
    # Does not work as intended
    # -- With all following test functions commented out, the "steak" and "fried chicken sandwhich" instances
    # -- of the meal class should be stored in food info.json. Instead, the only instance of the food class stored is "taco"
    # -- Somehow passes unittests...?
    def test_multiple_add(self):
        """Ability to write multiple instances of the Meal class to foodinfo.json"""

        meal0 = Meal("fried chicken sandwhich", "chicken", 2, 3) # --------------> Meal Object for Multiple Add Test (Goal: Add)
        meal1 = Meal("steak", "beef", 5, 1) # -----------------------------------> Meal Object for Multiple Add Test (Goal: Add)
        
        # -- Makes sure setUp() did its job
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 0)
        
        # -- Adds meal0 (fried chicken sandwich) to foodinfo.json and checks that there is only one item in the list
        self.data.meal_add(meal0)
        meal_gets = self.data.meal_get() 
        self.assertEqual(len(meal_gets), 1)

        # -- Adds meal1 (steak) to foodinfo.json and checks that there are two items in the list
        self.data.meal_add(meal1)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 2)
        
        # -- Checks that the first meal from foodinfo.json is meal0 (fried chicken sandwhich)
        self.assertEqual(meal_gets[0].name, meal0.name)
        
        # -- Checks that the second meal from foodinfo.json is meal1 (steak)
        self.assertEqual(meal_gets[1].name, meal1.name)
     
    
    # Works as intended
    def test_float(self):
        """Floats are rounded and converted into integers"""
        
        float = Meal("N/A", "N/A", 2.51, 2.51) # ---------------------------> Meal Object for Float to Integer Test (Goal: Round Values Up to an Integer)
        
        # -- Makes sure setUp() did its job
        self.assertEqual(self.data.meal_get(), self.emptylist)
        
        # -- Checks that both float values are rounded up to 3.0 and then converted to an integer (3)
        self.assertEqual(float.cost, 3)
        self.assertEqual(float.difficulty, 3)
    
    
    # Works as inteded
    def test_def_limit(self):
        """Cost and Difficulty values are between 1 and 5"""
        
        above_bound = Meal("N/A", "N/A", 10, 10) # -------------------------> Meal Object for Above Bounds Test (Both for Difficulty and Cost) (Goal: Correct to 5)
        below_bound = Meal("N/A", "N/A", -10, -10) # -----------------------> Meal Object for Below Bounds Test (Both for Difficulty and Cost) (Goal: Correct to 1)
        
        # -- Makes sure setUp() did its job
        self.assertEqual(self.data.meal_get(), self.emptylist)
        
        # -- Checks that the above bounds inputs for Cost and Difficulty are corrected to 5
        self.assertEqual(above_bound.cost, 5)
        self.assertEqual(above_bound.difficulty, 5)
        
        # -- Checks that the below bounds inputs for Cost and Difficulty are corrected to 1
        self.assertEqual(below_bound.cost, 1)
        self.assertEqual(below_bound.difficulty, 1)


    # Works as intended    
    def test_single_delete(self):
        """Taco meal should be removed from the list"""
        
        meal1 = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for Single Delete Test (Goal: Add then Remove)
        meal2 = Meal("fried chicken sandwhich", "chicken", 2, 3) # ---------> Meal Object for Single Delete Test (Goal: Add)
        meal3 = Meal("steak", "beef", 5, 1) # ------------------------------> Meal Object for Single Delete Test (Goal: Add)
        
        # -- Makes sure setUp() did its job
        self.assertEqual(self.data.meal_get(), self.emptylist)
        
        # -- Adds three instances of the Meal class to foodinfo.json
        self.data.meal_add(meal1)
        self.data.meal_add(meal2)
        self.data.meal_add(meal3)
        
        # -- Gets list of Meal objects and ensures that there are three items in the retrieved list
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 3)
        
        # -- Confirms the three returned Meal objects are the objects we expect back
        self.assertEqual(meal_gets[0].name, meal1.name)
        self.assertEqual(meal_gets[1].name, meal2.name)
        self.assertEqual(meal_gets[2].name, meal3.name)
        
        # -- Deletes a single Meal object (taco) from the list
        self.data.meal_del(meal1.name)
        
        # -- Gets the list of meal objects remaining and checks that they are the expected objects
        meal_gets = self.data.meal_get()
        self.assertEqual(meal_gets[0].name, meal2.name)
        self.assertEqual(meal_gets[1].name, meal3.name)   
    
    
    # Does not work as intended
    # -- With line 38 commented out, there should be one instance of the Meal class (steak) in a list inside foodinfo.json
    # -- Instead foodinfo.json contains a list with two instances of the meal class (one is steak) in a list inside foodinfo.json
    # -- Somehow, the code supposedly passes all tests
    def test_multiple_delete(self):
        """Taco and Fried Chicken Sandwhich should be removed from the list"""
        
        meal1 = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for Single Delete Test (Goal: Add then Remove)
        meal2 = Meal("fried chicken sandwhich", "chicken", 2, 3) # ---------> Meal Object for Single Delete Test (Goal: Add then Remove)
        meal3 = Meal("steak", "beef", 5, 1) # ------------------------------> Meal Object for Single Delete Test (Goal: Add)
        
        # -- Makes sure setUp() did its job
        self.assertEqual(self.data.meal_get(), self.emptylist)
        
        # -- Adds meal1 (taco) to foodinfo.json and checks that there is only one item in the list
        self.data.meal_add(meal1)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 1)
        
        # -- Adds meal2 (fried chicken sandwich) to foodinfo.json and checks that there are two items in the list
        self.data.meal_add(meal2)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 2)
        
        # -- Adds meal3 (steak) to foodinfo.json and checks that there are three items in the list
        self.data.meal_add(meal3)
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 3)
        
        # -- Gets the full list of meals
        meal_gets = self.data.meal_get()
        
        # -- Ensures all meals are in the expected order 
        self.assertEqual(meal_gets[0].name, meal1.name) 
        self.assertEqual(meal_gets[1].name, meal2.name) 
        self.assertEqual(meal_gets[2].name, meal3.name) 
        
        # -- Removes meal1 (taco) and meal2 (fried chicked sandwich) from the list and saves modified list to foodinfo.json
        self.data.meal_del(meal1.name)
        self.data.meal_del(meal2.name)
        
        # -- Ensures there is only one remaining item in the list
        meal_gets = self.data.meal_get()
        self.assertEqual(len(meal_gets), 1)
        
        # -- Ensures the remaining item is meal3 (steak)
        self.assertEqual(meal_gets[0].name, meal3.name)
  
if __name__ == '__main__':
    unittest.main()