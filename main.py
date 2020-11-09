from classes.Stock import Stock

class ProgrammePrincipal:
    def principal(self):
        S = Stock()
        while True:
            print("\n1 - voir le stock")
            print("2 - ajouter au stock")
            print("3 - retirer au stock")
            choix = input("> ")

            if choix == "1":
                S.affichierStock()

            elif choix == "2":
                S.ajoutComposant()


            elif choix == "3":
                print("\n1 - retirer processeur")
                print("2 - retirer carte graphique")
                print("3 - retirer hdd")
                print("4 - retirer RAM")
                composant = input("> ")

                if composant == "1":
                    S.retirerDuStock(S.processeur_stock)

                elif composant == "2":
                    S.retirerDuStock(S.carteGraphique_stock)

                elif composant == "3":
                    S.retirerDuStock(S.hdd_stock)

                elif composant == "4":
                    S.retirerDuStock(S.ram_stock)

                else:
                    pass

            else:
                break

a = ProgrammePrincipal()
a.principal()
