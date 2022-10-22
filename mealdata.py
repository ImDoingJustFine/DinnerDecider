from operator import index
from meal import Meal
import json

class Meal_Data:
    """Data layer to be used in conjunction with the Meal class"""

    def __init__(self, filename = "foodinfo.json"):
        """Initializes Meal_Data"""
        
        self.filename = filename


    def meal_add(self, meal:Meal) -> None:
        """Stores an instance of the Meal class inside foodinfo.json"""
        
        # -- Checks to see if a meal by the given name already exists
        dupe_check = self.meal_find(meal.name)
        
        # -- 'If' happens if no meal name matches the name given
        if dupe_check == None:
            meals = self.meal_get()
            meals.append(meal)
            self.meal_save(meals)
            
        # -- 'Else' happens if a mean name matches the name given
        else:
            error_message = f"A meal by the name '{meal.name.title()}' already exists."
            print(error_message)
            return

        
    def meal_save(self, meals:list) -> None:
        """Saves a list of meals to the JSON"""
        
        jsonmeals = []
        
        # -- Following for loop converts objects in meal list (jsonmeals) into dictionaries
        for mealobj in meals:
            jsonmeal = mealobj.as_dict()
            jsonmeals.append(jsonmeal)
        
        # -- Loads foodinfo.json and saves the list of Meal objects to it
        f = open(self.filename, 'w')
        f.flush()
        json.dump(jsonmeals, f, indent=2)
        f.close()
        
        # -- NNext line prints out to string the list of Meals in JSON format
        # print(json.dumps(jsonmeals, indent=2))
        return
            
    # -- TODO : make a function to delete a Meal object that is stored inside foodinfo.json
    def meal_del(self, name:str) -> None:
        """Removes an instance of the Meal class inside foodinfo.json"""
        
        meals = self.meal_get()

        # -- Loop over all meals and remove 
        for meal in meals:
            if meal.name == name:
                index = meals.index(meal)
                del meals[index]
            else: 
                pass
        # -- END FOR
        
        # -- Saves changed list to foodinfo.json
        self.meal_save(meals)
 

    def meal_get(self) -> list[Meal]:
        """Returns a list of meals"""
        
        # -- Tries to open foodinfo.json and creates a new foodinfo.json if it cannot be found as well as return an empty list (jsondata) when relevant
        try:
            f = open(self.filename)
        except FileNotFoundError:
            error_message = f"\nFile {self.filename} was not found.\n"
            print(error_message)
            return []

        # Explicit flush to ensure we have the latest version of the file on disk
        f.flush()        

        # -- Tries to load foodinfo.json and returns an empty list (jsondata) when relevant
        try:
            jsondata = json.load(f)
        except json.JSONDecodeError:
            jsondata = []

        # Manually closes foodinfo.json
        f.close()

        # -- The folowing for loop takes the JSON objects found in foodinfo.json and turns them into Python objects
        # -- and then appends those objects into the meals list and returns said list    
        meals = []
        for item in jsondata:
            meal = Meal(item['name'],item['protein'],item['cost'],item['difficulty'])
            meals.append(meal)
        
        return meals
    
    
    def meal_find(self, name:str) -> Meal:
        """Returns a specific meal object when searching for a meal by name"""
        
        # -- Gets full list of Meal objects from foodinfo.json
        meals = self.meal_get()
    
        # -- The following for loop cycles through the meals list looking for a matching meal name
        # -- If the meal name inquired is not found - the loop will return None
        for obj in meals:
            if obj.name == name:
                return obj
            else:
                return None