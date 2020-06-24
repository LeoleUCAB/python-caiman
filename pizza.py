from food import Food

class Pizza(Food):
    """docstring for Pizza"""

    def __init__(self, price, name):
        super(Pizza, self).__init__(price, name)

    def cost(self, size):
        return super().cost(size)

    def name(self):
        return super().name()

    def size(self):
        sizeString = super().name()[0]
        sizeDict = {
            'personal': 0,
            'mediana': 1,
            'familiar': 2
        }
        return sizeDict[sizeString.lower()]
