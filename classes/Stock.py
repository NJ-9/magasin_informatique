"""
module for creating a stock object to manage stock
"""

from classes.ram import RAM
from classes.hdd import HDD
from classes.processor import Processor
from classes.graphic_card import GraphicCard


class Stock:

    """
    class for creating a stock object
    """

    def __init__(self):

        """
        method doctring
        """

        self.processor_stock = {}
        self.graphic_card_stock = {}
        self.hdd_stock = {}
        self.ram_stock = {}
        self.stock_remove = {}

    def add_component(self):

        """
        method doctring
        """

        print("\n1 - add processor")
        print("2 - add graphic card")
        print("3 - add hdd")
        print("4 - add RAM")
        add_component = input("> ")
        choice_brand = input("Which brand do you want to add > ")
        if choice_brand != "":
            nb_component = int(input("How many do you want > "))

        if add_component == "1":
            component = Processor(nb_component, choice_brand)
            component_stock = self.processor_stock

        elif add_component == "2":
            component = GraphicCard(nb_component, choice_brand)
            component_stock = self.graphic_card_stock

        elif add_component == "3":
            component = HDD(nb_component, choice_brand)
            component_stock = self.hdd_stock

        elif add_component == "4":
            component = RAM(nb_component, choice_brand)
            component_stock = self.ram_stock

        else:
            print("Wrong input")

        if component.brand in component_stock:
            components_in_stock = component_stock[component.brand]
            number = component.number + components_in_stock
            component_stock.update({component.brand: number})
        else:
            component_stock[component.brand] = component.number

    def show_stock(self):

        """
        method doctring
        """

        print("\nprocessor : ", self.processor_stock)
        print("graphic card : ", self.graphic_card_stock)
        print("hdd : ", self.hdd_stock)
        print("ram : ", self.ram_stock, '\n')

    def remove_from_stock(self, stock):

        """
        method doctring
        """
        if stock in self.stock_check():
            name = input("Which brand do you want to remove : ")
            if name in stock:
                nb_component = stock[name]
                number = int(input("How much do you want to remove : "))
                if number <= nb_component:
                    final_stock = nb_component - number
                    stock[name] = final_stock
                else:
                    print("You don't have enough stock")
            else:
                print("There is no components ", name, " here !")
        else:
            print("Unknown stock")

    def stock_check(self):
        """
        method doctring
        """
        stock = [
            self.processor_stock,
            self.graphic_card_stock,
            self.hdd_stock,
            self.ram_stock
                ]
        return stock
