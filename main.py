"""
module docstring
"""
from classes.stock import Stock



class MainProgram:
    """
    class docstring
    """
    def __init__(self):
        self.stock = Stock()
        self.main()



    def main(self):
        """
        mathod docstring
        """
        while True:
            print("\n1 - see the stock")
            print("2 - add to stock")
            print("3 - remove from stock")
            choice = input("> ")
            if choice == "1":
                self.stock.show_stock()
            elif choice == "2":
                self.stock.add_component()
            elif choice == "3":
                print("\n1 - remove processor")
                print("2 - remove graphic card")
                print("3 - remove hdd")
                print("4 - remove RAM")
                component = input("> ")
                self.remove_from_stock(component)
            else:
                break



    def remove_from_stock(self, component):
        """
        mathod docstring
        """
        if component == "1":
            self.stock.remove_from_stock(self.stock.processor_stock)
        elif component == "2":
            self.stock.remove_from_stock(self.stock.graphic_card_stock)
        elif component == "3":
            self.stock.remove_from_stock(self.stock.hdd_stock)
        elif component == "4":
            self.stock.remove_from_stock(self.stock.ram_stock)



if __name__ == "__main__":
    MainProgram()
