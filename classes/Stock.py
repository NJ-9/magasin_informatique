from classes.ram import RAM
from classes.hdd import HDD
from classes.Processeur import Processeur
from classes.CarteGraphique import CarteGraphique


class Stock:
    def __init__(self):
        self.processeur_stock = {}
        self.carteGraphique_stock = {}
        self.hdd_stock = {}
        self.ram_stock = {}

    def ajoutComposant(self):
        print("\n1 - ajout processeur")
        print("2 - ajout carte graphique")
        print("3 - ajout hdd")
        print("4 - ajout RAM")
        ajout_composant = input("> ")
        choix_marque = input("quelle marque voulez vous ajouter > ")
        if choix_marque != "":
            nb = int(input("combien en voulez vous"))

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
