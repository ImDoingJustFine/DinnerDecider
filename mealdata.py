from operator import index
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
        
        dupe_check = self.meal_find(meal.name)
        if dupe_check == None:
            meals = self.meal_get()
            meals.append(meal)
            self.meal_save(meals)
        else:
            error_message = f"A meal by the name '{meal.name.title()}' already exists."
            print(error_message)
            return

        
    def meal_save(self, meals:list) -> None:
        """Saves a list of meals to the JSON"""
        
        jsonmeals = []
        # -- Following for loop converts objects in meal list (jsonmeals) into dictionaries --
        for mealobj in meals:
            jsonmeal = mealobj.as_dict()
            jsonmeals.append(jsonmeal)
        # -- Following two lines converts the list of dictionaries made above into JSON format and saves to foodinfo.json --
        with open(self.filename, 'w') as f:
            json.dump(jsonmeals, f, indent=2)
        # -- Next two lines print out to string the list of Meals in JSON format --
        # jsondump = json.dumps(jsonmeals, indent=2)
        # print(jsondump)
        return
            
    # -- TODO : make a function to delete a Meal object that is stored inside foodinfo.json --
    def meal_del(self, name:str):
        """Removes an instance of the Meal class inside foodinfo.json"""
        
        meals = self.meal_get()

        # Loop over all meals and remove 
        for meal in meals:
            if meal.name == name:
                index = meals.index(meal)
                del meals[index]
            else: 
                pass
        # END FOR
        
        self.meal_save(meals)
 

    def meal_get(self) -> list[Meal]:
        """Returns a list of meals"""
        
        
        try:
            with open(self.filename) as f:
                jsondata = json.load(f)
        # -- TODO : If the foodinfo.json is not found it should make a .json file by that name --
        except FileNotFoundError:
            error_message = f"\nFile {self.filename} was not found.\n"
            print(error_message)
            return []
        # -- When the following error occurs, the list of meals is simply left as an empty list --
        except json.JSONDecodeError:
            # crete empty JSONData for following loop
            jsondata = []

        # -- The folowing for loop takes the JSON objects found in foodinfo.json and turns them into Python objects --
        # -- and then appends those objects into the meals list        
        meals = []
        for item in jsondata:
            meal = Meal(item['name'],item['protein'],item['cost'],item['difficulty'])
            meals.append(meal)
        return meals
    
    
    def meal_find(self, name:str) -> Meal:
        """Returns a specific meal object when searching for a meal by name"""
        
        meals = self.meal_get()
        # -- The following for loop cycles through the meals list looking for a matching meal name
        # -- If the meal name inquired is not found - the loop will return None
        for obj in meals:
            if obj.name == name:
                return obj
        return None       