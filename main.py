from classes.Stock import Stock

class MainProgram:
    def main(self):
        S = Stock()
        while True:
            print("\n1 - see the stock")
            print("2 - add to stock")
            print("3 - remove from stock")
            choice = input("> ")

            if choice == "1":
                S.showStock()

            elif choice == "2":
                S.addcomponent()


            elif choice == "3":
                print("\n1 - remove processor")
                print("2 - remove graphic card")
                print("3 - remove hdd")
                print("4 - remove RAM")
                component = input("> ")

                if component == "1":
                    S.RemoveFromStock(S.processor_stock)

                elif component == "2":
                    S.RemoveFromStock(S.graphicCard_stock)

                elif component == "3":
                    S.RemoveFromStock(S.hdd_stock)

                elif component == "4":
                    S.RemoveFromStock(S.ram_stock)

                else:
                    pass

            else:
                break

a = MainProgram()
a.main()
