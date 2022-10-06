from distutils.log import error
from meal import Meal
import json

class Meal_Data:

    filename = "foodinfo.json"

    def __init__(self):
        """Initializes Meal_Data"""
        pass

    def meal_add(self, meal:Meal):
        """Stores an instance of the Meal class inside foodinfo.json"""
        try:
            jsondata = self.meal_get()
            jsondata.append(meal)
        except AttributeError:
            error_message = "\nThere was an AttributeError. Unable to add meal.\
                \n'jsondata' does not have append attribute (jsondata != list)\n"
            print(error_message)
            return
        
        with open(self.filename, 'w') as f:
            json.dump(jsondata, f, indent=2)

    # def meal_del(self):
    #     """Removes an instance of the Meal class inside foodinfo.json"""
 
    def meal_get(self):
        """Returns a list of meals"""

        try:
            with open(self.filename) as f:
                jsondata = json.load(f)
        except FileNotFoundError:
            error_message = "\nFile foodinfo.json was not found.\n"
            print(error_message)
            return
        except json.JSONDecodeError:
            error_message = "\nThere was a json.JSONDecodeError:\
                \nCould be an empty file or corrupted file.\n"
            print(error_message)
            return
        else:
            return jsondata

        # meallist = []

        # try:
        #     with open(self.filename, 'w') as f:
        #         jsondata = json.load(f)
        # except FileNotFoundError:
        #     print(f"It looks like '{self.filename}' was not found.")
        # else:
        #     for meal in jsondata:
        #         meal_obj = Meal(meal['name'], meal['protein'], meal['difficulty'], meal['cost'])
        #         meallist.append(meal_obj)
        #     return meallist