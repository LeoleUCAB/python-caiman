from main import *

lista = open('./pedidos/pedidos1.pz').readlines()
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
        print("ARCHIVO NO VÁLIDO")

for pizza in listaPizzas:
    if listaPizzas.index(pizza) != 0:
        print(pizza.recipe())
