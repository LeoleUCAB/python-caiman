from food import Pizza, Ingredient, Decorator
import tkinter
from tkinter import filedialog
import os


def searchForFilePath():
    main_win = tkinter.Tk() 
    main_win.withdraw()

    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')

    main_win.deiconify()
    main_win.lift()
    main_win.focus_force()

    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, 
    initialdir= "/", title='Please select a directory')

    main_win.destroy()
    return main_win.sourceFile


def fileToObject(route):
    try:
        lista = open(route).readlines()
    except UnicodeDecodeError:
        return None
    pedidos = [x.replace('\n', '') for x in lista]
    print(pedidos)
    i = 0
    listaPizzas = []
    while(i < len(pedidos)):
        if pedidos[i] == 'COMIENZO_PEDIDO':
            j = i+2
            # A dos líneas del comienzo se encuentran las pizzas
            while(pedidos[j] != 'FIN_PEDIDO'):
                orden = pedidos[j].split(";")
                # Separa la pizza y extras en una lista
                pizza = Pizza([10, 15, 20], orden[0])
                orden.remove(orden[0])
                for extra in orden:
                    # Agrega cada ingrediente a la pizza
                    ingrediente = Ingredient([1.5, 1.75, 2], extra)
                    pizza = Decorator(pizza, ingrediente)
                listaPizzas.append(pizza)
                j = j+1
            i = j+1
        else:
            return None
    return listaPizzas


def showPizzaList(listaPizzas):
    for pizza in listaPizzas:
        if type(pizza) == Decorator:
            print(pizza.recipe())
        else:
            print("Una pizza", pizza.name()[0], "sin extras")
