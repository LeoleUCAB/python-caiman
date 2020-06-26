from pizza import Pizza
from ingredient import Ingredient
from decorator import Decorator
from order import Order
from dataBase import insert_order, insert_pizza, select_last_inserted_pizza, select_pizza_size, insert_pizza_ingredient, create_connection
import tkinter
from tkinter import filedialog
import os
import sqlite3

database = r"./dataBase/pizzaDataBase.db"

def searchForFilePath():
    main_win = tkinter.Tk()
    main_win.withdraw()

    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')

    main_win.deiconify()
    main_win.lift()
    main_win.focus_force()

    main_win.sourceFile = filedialog.askopenfilename(
        parent=main_win,
        initialdir="/", title='Please select a directory')

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
    listaOrdenes = []
    while(i < len(pedidos)):
        if pedidos[i] == 'COMIENZO_PEDIDO':
            
            j = i+2
            # A dos líneas del comienzo se encuentran las pizzas
            listaPizzas = []
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
            order = Order(pedidos[i+1].split(";")[1], listaPizzas)
            listaOrdenes.append(order)
            i = j+1
        else:
            return None
    return listaOrdenes


def showPizzaList(listaPizzas):
    for pizza in listaPizzas:
        if type(pizza) == Decorator:
            print(pizza.recipe())
        elif type(pizza) == Order:
            print(pizza.fecha())
        else:
            print("Una pizza", pizza.name()[0], "sin extras")


def showOrders(ordenes):
    connection = create_connection(database)
    for orden in ordenes:
        print(orden.fecha())
        id_order = insert_order(connection, orden)
        print(f'el id es ${id_order}')
        for pizza in orden.listaPizzas():
            pizzaNumber = select_last_inserted_pizza(connection) + 1
            if type(pizza) == Decorator:
                print(pizza.recipe())
                insert_pizza_ingredient(connection, pizza, pizzaNumber, id_order)
            else:
                insert_pizza(connection, pizza, pizzaNumber, id_order)
                print("Una pizza", pizza.name()[0], "sin extras")
