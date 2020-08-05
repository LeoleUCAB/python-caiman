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
