class Order(object):

    def __init__(self, fecha, listaPizzas):
        super(Order, self).__init__()
        self.__fecha = fecha
        self.__listaPizzas = listaPizzas

    def fecha(self):
        return self.__fecha

    def listaPizzas(self):
        return self.__listaPizzas
