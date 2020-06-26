from pizza import Pizza
from ingredient import Ingredient
from decorator import Decorator
from order import Order
from dataBase import select_report_ingredient, select_report_pizza
import tkinter
from tkinter import filedialog
import os


def generateReport(source):
    f = open(source+'/report.txt', "w")
    
    rows = select_report_pizza()
    rows_in = select_report_ingredient()
    rows_date_template = 0
    for row in rows:
        f.write("\n")
        if rows_date_template == 0 or rows_date_template != row[1]:
            f.write(f'fecha: {row[1]}\n\n')

            f.write("Ventas por pizza (sin incluir adicionales)\n")
            f.write("TAMAÑO     UNIDADES      MONTO \n")
            rows_date_template = row[1]
        f.write(row[0]+"       "+str(row[2])+"          "+str(row[3])+"\n")
    rows_date_template = 0
    for row in rows_in:
        f.write("\n")
        if rows_date_template == 0 or rows_date_template != row[1]:
            f.write(f'fecha: {row[1]}\n\n')

            f.write("Ventas por ingrediente \n")
            f.write("Ingrediente     UNIDADES      MONTO \n")
            rows_date_template = row[1]
        f.write(row[0]+"       "+str(row[2])+"          "+str(row[3])+"\n")
    f.close()


def searchForReportPath():
    main_win = tkinter.Tk()
    main_win.withdraw()

    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')

    main_win.deiconify()
    main_win.lift()
    main_win.focus_force()

    main_win.sourceFile = filedialog.askdirectory(
        parent=main_win,
        initialdir="/", title='Please select a directory')

    main_win.destroy()
    return main_win.sourceFile
