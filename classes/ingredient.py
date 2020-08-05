from food import Food

class Ingredient(Food):
    """docstring for Ingredient"""

    def __init__(self, price, name):
        super(Ingredient, self).__init__(price, name)

    def cost(self, size):
        return super().cost(size)

    def name(self):
        return super().name()