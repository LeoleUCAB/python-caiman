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
