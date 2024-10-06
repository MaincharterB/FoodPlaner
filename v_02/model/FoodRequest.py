from typing import List
from v_02.model import MealItem, Nutrition, PreferDislike


class FoodRequest:
    def __init__(self, nutrition_data: Nutrition, preffers: PreferDislike = None, dislikes: PreferDislike = None, meals_data: List = None ):
        self.nutrition_data = nutrition_data
        self.preffers = preffers
        self.dislikes = dislikes
        self.meals_data = meals_data