from classes.ram import RAM
from classes.hdd import HDD
from classes.Processor import Processor
from classes.GraphicCard import GraphicCard


class Stock:
    def __init__(self):
        self.processor_stock = {}
        self.graphicCard_stock = {}
        self.hdd_stock = {}
        self.ram_stock = {}

    def addcomponent(self):
        print("\n1 - add processor")
        print("2 - add graphic card")
        print("3 - add hdd")
        print("4 - add RAM")
        add_component = input("> ")
        choice_brand = input("Which brand do you want to add > ")
        if choice_brand != "":
            nb = int(input("How many do you want > "))

        if add_component == "1":
            component = Processor(nb, choice_brand)
            componentStock = self.processor_stock

        elif add_component == "2":
            component = GraphicCard(nb, choice_brand)
            componentStock = self.graphicCard_stock

        elif add_component == "3":
            component = HDD(nb, choice_brand)
            componentStock = self.hdd_stock

        elif add_component == "4":
            component = RAM(nb, choice_brand)
            componentStock = self.ram_stock

        else:
            print("Wrong input")

        if component.brand in componentStock:
            componentsInStock = componentStock[component.brand]
            number = component.number + componentsInStock
            componentStock.update({a.brand: number})
            return componentStock
        else:
            componentStock[component.brand] = component.number
            return componentStock

    def showStock(self):
        print("\nprocessor : ", self.processor_stock)
        print("graphic card : ", self.graphicCard_stock)
        print("hdd : ", self.hdd_stock)
        print("ram : ", self.ram_stock, '\n')

    def RemoveFromStock(self, stock):
        name = input("Which brand do you want to remove : ")
        if name in stock:
            nb = stock[name]
            number = int(input("How much do you want to remove : "))
            if number <= nb:
                final_stock = nb - number
                stock[name] = final_stock
            else:
                print("You don't have enough stock")
        else:
            print("There is no components ", name, " here !")
