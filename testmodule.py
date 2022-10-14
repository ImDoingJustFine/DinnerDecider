from meal import Meal
from mealdata import Meal_Data
import json
import unittest

    #>-----------------------------------------------------------<#
    #  Predefined objects of the Meal Class for testing purposes  #
    #>-----------------------------------------------------------<#

addtest = Meal("taco", "ground", 1, 2) # -----------------------------> Meal Object for "Single Add Test"
addtest2 = Meal("steak", "beef", 5, 1) # -----------------------------> Meal Object for "Multiple Add Test"
addtest3 = Meal("fried chicken sandwhich", "chicken", 2, 3) # --------> Meal Object for "Multiple Add Test"
float = Meal("N/A", "N/A", 2.5, 3.1) # -------------------------------> Meal Object for "Float to Integer Test"
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
    
    
    def single_add_test(self, meal:Meal):
        """Tests adding and getting data from foodinfo.json in the case of a single Meal object"""
        
        checklist = [False, False, False, False]
        expectedlist = [True, True, True, True]
        
        self.clean_slate_test()
        self.data.meal_add(meal)
        mealget = self.data.meal_get()
        if meal.name == mealget[0].name:
            checklist[0] = True
        if meal.protein == mealget[0].protein:
            checklist[1] = True
        if meal.cost == mealget[0].cost:
            checklist[2] = True
        if meal.difficulty == mealget[0].difficulty:
            checklist[3] = True
        if checklist == expectedlist:
            checkmessage = f"Pass."
            return checkmessage
        else:
            checkmessage = f"Fail:\n'{meal.name.title()}' has failed to be added to {self.filename}'."
            return checkmessage
    
    
    def multiple_add_test(self, meal1:Meal, meal2:Meal):
        """Tests adding and getting data from foodinfo.json in the case of multiple Meal objects"""

        checklist = [False, False]
        failedlist1 = [True, False]
        failedlist2 = [False, True]
        expectedlist = [True, True]
        
        self.clean_slate_test()        
        if self.single_add_test(meal1) == "'Steak' has succsefully been added to 'foodinfo.json'.":
            checklist[0] = True
        if self.single_add_test(meal2) == "'Fried Chicken Sandwhich' has succsefully been added to 'foodinfo.json'.":
            checklist[1] = True
        if checklist == expectedlist:
            checkmessage = f"Pass."
            return checkmessage
        if checklist == failedlist1:
            checkmessage = f"Fail:\n'{meal1.name.title()}' was succsefully added to '{self.filename}' but '{meal2.name.title()}' was not."
            return checkmessage
        if checklist == failedlist2:
            checkmessage = f"Fail:\n'{meal2.name.title()}' was succsefully added to '{self.filename}' but '{meal1.name.title()}' was not."
            return checkmessage
        else:
            checkmessage = f"Fail:\nNeither '{meal1.name.title()}' or '{meal2.name.title()}' were saved to '{self.filename}'."
            return checkmessage
        
        
    def float_test(self, meal:Meal):
        """Makes sure that floats are rounded and converted into integers"""
        
        checklist = [False, False]
        failedlist1 = [True, False]
        failedlist2 = [False, True]
        expectedlist = [True, True]        
        
        if meal.cost == int(meal.cost):
            checklist[0] = True
        if meal.difficulty == int(meal.difficulty):
            checklist[1] = True
        if checklist == expectedlist:
            checkmessage = "Pass"
            return checkmessage
        if checklist == failedlist1:
            checkmessage = "Cost is an integer but Difficulty is still a float."
            return checkmessage
        if checklist == failedlist2:
            checkmessage = "Difficulty is an integer, but Cost is still a float."
            return checkmessage
        else:
            checkmessage = "Both values are still floats"
    
    # def def_limit_test(self, meal:Meal):
    #     """Makes sure that Cost and Difficulty values are between 1 and 5"""
        
    #     checklist1 = [False, False]
    #     checklist2 = [False, False]
    #     expectedlist = [True, True]
        
    #     if meal.cost > 1:
    #         checklist1[0] = True
    #     if meal.cost < 5:
    #         checklist1[1] = True
    #     if meal.difficulty >
    #     if checklist1 and checklist2 == expectedlist:
    #         checkmessage = "Pass."
    #         return checkmessage
        
        
codetest = TestCases()
print("\n# -- Test 1 : Single 'meal_add' Function -- #")
print(codetest.single_add_test(addtest))
print("\n# -- Test 2 : Multiple 'meal_add' Functions -- #")
print(codetest.multiple_add_test(addtest2, addtest3))
print("\n# -- Test 3 : Cost and Difficulty == Int? -- #")
print()
print("\n# -- Test 4 : Cost and Difficulty Within Limits? -- #")
print()