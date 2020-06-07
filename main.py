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

    def __init__(self, price, size):
        super(Pizza, self).__init__()
        self.__price = price
        self.__size = size

    def cost(self, size):
        return self.__price[size]

    def name(self):
        return [self.__size]

    def size(self):
        sizeDict = {
            'personal': 0,
            'mediana': 1,
            'familiar': 2
        }
        return sizeDict[self.__size.lower()]


class Ingredient(Food):
    """docstring for Ingredient"""

    def __init__(self, price, name):
        super(Ingredient, self).__init__()
        self.__price = price
        self.__name = name

    def cost(self, size):
        return self.__price[size]

    def name(self):
        return [self.__name]


class Decorator(object):
    """docstring for Decorator"""

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

    def __prettyIngredients(self, duplicates):
        for name, count in duplicates.items():
            if count < 2:
                yield name
            elif count < 5:
                yield numerals[count] + ' ' + name
            else:
                yield numerals[5] + ' ' + name


if __name__ == "__main__":
    largePizza = Pizza([10, 15, 20], 'Familiar')
    jamon = Ingredient([1.5, 1.75, 2], 'jamón')
    champinones = Ingredient([1.75, 2.05, 2.5], 'champiñones')
    pimenton = Ingredient([1.5, 1.75, 2], 'pimentón')
    myPizza = Decorator(largePizza, jamon)
    myPizza = Decorator(myPizza, jamon)
    myPizza = Decorator(myPizza, jamon)
    myPizza = Decorator(myPizza, pimenton)
    myPizza = Decorator(myPizza, pimenton)
    myPizza = Decorator(myPizza, pimenton)
    myPizza = Decorator(myPizza, pimenton)
    myPizza = Decorator(myPizza, pimenton)
    myPizza = Decorator(myPizza, champinones)
    myPizza = Decorator(myPizza, champinones)
    print(myPizza.cost())
    print(myPizza.name())
    print(myPizza.recipe())
