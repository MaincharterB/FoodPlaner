from v_02.model import Nutrition, PreferDislike

class MealItem:
    def __init__(self, nutrition_data: Nutrition, dish_count: int, complex_dish_count: int, preffers: PreferDislike, dislikes: PreferDislike):
        self.nutrition_data = nutrition_data
        self.dish_count = dish_count
        self.complex_dish_count = complex_dish_count
        self.preffers = preffers
        self.dislikes = dislikes

