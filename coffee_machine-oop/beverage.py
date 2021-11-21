class Beverage:
    def __init__(self, name, ingredients, cost):
        self.__name = name
        self.__ingredients = ingredients
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_cost(self):
        return self.__cost
