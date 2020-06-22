from food import Pizza, Ingredient, Decorator
from readFile import searchForFilePath, fileToObject, showPizzaList

if __name__ == "__main__":
    while True:
        print("""
        Bienvenido a la pizzería
        1. Para subir archivo
        0. Salir""")
        menuOption = int(input("Elija una opción: "))
        if menuOption == 0:
            break
        elif menuOption == 1:
            pizzaList = fileToObject(searchForFilePath())
            if pizzaList is None:
                print("Archivo no válido")
            else:
                showPizzaList(pizzaList)

    
    """
    myPizza = Pizza([10, 15, 20], 'Familiar')
    jamon = Ingredient([1.5, 1.75, 2], 'jamón')
    champinones = Ingredient([1.75, 2.05, 2.5], 'champiñones')
    pimenton = Ingredient([1.5, 1.75, 2], 'pimentón')
    myPizza = Decorator(myPizza, jamon)
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
    print(myPizza.recipe())"""
