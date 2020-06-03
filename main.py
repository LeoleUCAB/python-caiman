numerals = {
    2: 'doble',
    3: 'triple',
    4: 'quádruple',
    5: 'exceso de'
}


class Food:
    """docstring for Food"""

    def __init__(self):
        super(Food, self).__init__()

    def cost(self):
        pass


class Pizza(Food):
    """docstring for Pizza"""

    def __init__(self, price, name):
        super(Pizza, self).__init__()
        self.__price = price
        self.__name = name

    def cost(self):
        return self.__price

    def name(self):
        return [self.__name]


class Ingredient(Food):
    """docstring for Ingredient"""

    def __init__(self, price, name):
        super(Ingredient, self).__init__()
        self.__price = price
        self.__name = name

    def cost(self):
        return self.__price

    def name(self):
        return [self.__name]


class Decorator(object):
    """docstring for Decorator"""

    def __init__(self, pizza, ingredient):
        super(Decorator, self).__init__()
        self.__pizza = pizza
        self.__ingredient = ingredient

    def cost(self):
        return self.__pizza.cost() + self.__ingredient.cost()

    def name(self):
        return self.__pizza.name() + self.__ingredient.name()

    def recipe(self):
        ingredientList = self.name()
        # Se ignora el primer valor, ya que este contiene la pizza como tal
        duplicates = {i: ingredientList.count(i) for i in ingredientList[1:]}
        recipeList = list()
        recipeList.extend(self.__prettyIngredients(duplicates))
        recipeString = 'Una ' + ingredientList[0] + ' con '
        recipeString += ', '.join(recipeList[:-1])
        recipeString += ' y ' + recipeList[-1]
        return recipeString

    def __prettyIngredients(self, duplicates):
        for name, count in duplicates.items():
            if count < 2:
                yield name
            elif count < 5:
                yield numerals[count] + ' ' + name
            else:
                yield numerals[5] + ' ' + name


if __name__ == "__main__":
    largePizza = Pizza(100, 'pizza grande')
    anchovies = Ingredient(10, 'anchoas')
    pepperoni = Ingredient(15, 'pepperoni')
    pineapple = Ingredient(50, 'piña')
    myPizza = Decorator(largePizza, anchovies)
    myPizza = Decorator(myPizza, pineapple)
    myPizza = Decorator(myPizza, anchovies)
    myPizza = Decorator(myPizza, pepperoni)
    myPizza = Decorator(myPizza, pineapple)
    myPizza = Decorator(myPizza, pineapple)
    myPizza = Decorator(myPizza, pineapple)
    myPizza = Decorator(myPizza, anchovies)
    myPizza = Decorator(myPizza, pineapple)
    myPizza = Decorator(myPizza, pepperoni)
    print(myPizza.cost())
    print(myPizza.name())
    print(myPizza.recipe())
