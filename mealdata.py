from meal import Meal
import json

class Meal_Data:
    """Data layer to be used in conjunction with the Meal class"""
    
    filename = "foodinfo.json"

    def __init__(self):
        """Initializes Meal_Data"""
        
        pass


    def meal_add(self, meal:Meal):
        """Stores an instance of the Meal class inside foodinfo.json"""
        
        jsonmeals = []
        
        meals = self.meal_get()
        meals.append(meal)
        for mealobj in meals:
            jsonmeal = mealobj.as_dict()
            jsonmeals.append(jsonmeal)
            
        with open(self.filename, 'w') as f:
            json.dump(jsonmeals, f, indent=2)
            
        jsondump = json.dumps(jsonmeals, indent=2)
        print(jsondump)
            
            
    # def meal_del(self):
    #     """Removes an instance of the Meal class inside foodinfo.json"""
 
 
    def meal_get(self):
        """Returns a list of meals"""

        meals = []

        try:
            with open(self.filename) as f:
                jsondata = json.load(f)
        except FileNotFoundError:
            error_message = f"\nFile {self.filename} was not found.\n"
            print(error_message)
            return
        except json.JSONDecodeError:
            pass
        else:
            for item in jsondata:
                meal = Meal(item['name'],item['protein'],item['cost'],item['difficulty'])
                meals.append(meal)
        return meals