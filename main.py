class Stock:
    def __init__(self):
        self.processeur_stock = {}
        self.carteGraphique_stock = {}
        self.hdd_stock = {}
        self.ram_stock = {}

    def ajoutComposant(self):
        choix_marque = input("quelle marque voulez vous ajouter > ")
        if choix_marque != "":
            nb = int(input("combien en voulez vous"))

            print("\n1 - ajout processeur")
            print("2 - ajout carte graphique")
            print("3 - ajout hdd")
            print("4 - ajout RAM")
            ajout_composant = input("> ")

            if ajout_composant == "1":
                composant = Processeur(nb, choix_marque)
                composantStock = self.processeur_stock

            elif ajout_composant == "2":
                composant = CarteGraphique(nb, choix_marque)
                composantStock = self.carteGraphique_stock

            elif ajout_composant == "3":
                composant = HDD(nb, choix_marque)
                composantStock = self.hdd_stock

            elif ajout_composant == "4":
                composant = RAM(nb, choix_marque)
                composantStock = self.ram_stock

            else:
                print("Mauvaise entrée")

            if composant.marque in composantStock:
                composantsEnStock = composantStock[composant.marque]
                nombre = composant.nombre + composantsEnStock
                composantStock.update({a.marque: nombre})
                return composantStock
            else:
                composantStock[composant.marque] = composant.nombre
                return composantStock

    def affichierStock(self):
        print("\nprocesseur : ", self.processeur_stock)
        print("carte graphique : ", self.carteGraphique_stock)
        print("hdd : ", self.hdd_stock)
        print("ram : ", self.ram_stock, '\n')

    def retirerDuStock(self, stock):
        nom = input("quelle marque voulez vous retirer : ")
        if nom in stock:
            nb = stock[nom]
            nombre = int(input("combien voulez vous en retirer : "))
            if nombre <= nb:
                stock_final = nb - nombre
                stock[nom] = stock_final
            else:
                print("Vous n'avez pas assez de stock")
        else:
            print("Il n'y a pas de composant de marque ", nom, " ici !")

class Processeur:
    def __init__(self, nombre, marque):
        self.nombre = nombre
        self.marque = marque

class CarteGraphique:
    def __init__(self, nombre, marque):
        self.nombre = nombre
        self.marque = marque

class HDD:
    def __init__(self, nombre, marque):
        self.nombre = nombre
        self.marque = marque

class RAM:
    def __init__(self, nombre, marque):
        self.nombre = nombre
        self.marque = marque

if __name__ == "__main__":
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
