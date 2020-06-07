from abc import ABC, abstractmethod


class Food(ABC):
    """docstring for Food"""

    def __init__(self, price, name=None):
        super(Food, self).__init__()
        self.__price = price
        self.__name = name

    @abstractmethod
    def cost(self, size):
        return self.__price[size]

    @abstractmethod
    def name(self):
        return [self.__name]


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


class Ingredient(Food):
    """docstring for Ingredient"""

    def __init__(self, price, name):
        super(Ingredient, self).__init__(price, name)

    def cost(self, size):
        return super().cost(size)

    def name(self):
        return super().name()


class Decorator(object):
    """docstring for Decorator"""

    numerals = {
        2: 'doble',
        3: 'triple',
        4: 'quádruple',
        5: 'exceso de'
    }

    def __init__(self, pizza, ingredient):
        super(Decorator, self).__init__()
        self.__pizza = pizza
        self.__ingredient = ingredient

    def cost(self, size=None):
        if size is None:
            size = self.__pizza.size()
        return self.__pizza.cost(size) + self.__ingredient.cost(size)

    def size(self):
        return self.__pizza.size()

    def name(self):
        return self.__pizza.name() + self.__ingredient.name()

    def recipe(self):
        ingredientList = self.name()
        # Se ignora el primer valor, ya que este contiene la pizza como tal
        duplicates = {i: ingredientList.count(i) for i in ingredientList[1:]}
        recipeList = list()
        recipeList.extend(self.__prettyIngredients(duplicates))
        recipeString = 'Una pizza ' + ingredientList[0] + ' con '
        if len(ingredientList) > 2:
            recipeString += ', '.join(recipeList[:-1])
            recipeString += ' y ' + recipeList[-1]
        else:
            # Para imprimir bien la receta de pizzas con solo un extra
            recipeString += ingredientList[1]
        return recipeString

    @classmethod
    def __prettyIngredients(cls, duplicates):
        for name, count in duplicates.items():
            if count < 2:
                yield name
            elif count < 5:
                yield cls.numerals[count] + ' ' + name
            else:
                yield cls.numerals[5] + ' ' + name
