class Stock:
    def __init__(self):
        self.processeur_stock = {}
        self.carteGraphique_stock = {}
        self.hdd_stock = {}
        self.ram_stock = {}

    def ajoutProcesseur(self):
        CPU = input("quelle marque de processeur voulez vous ajouter > ")
        if CPU != "":
            nbCPU = int(input("combien en voulez vous"))
            a = Processeur(nbCPU, CPU)
            if CPU in self.processeur_stock:
                composantsEnStock = self.processeur_stock[CPU]
                nombre = a.nombre + composantsEnStock
                self.processeur_stock.update({a.marque: nombre})
                return self.processeur_stock
            else:
                self.processeur_stock[a.marque] = a.nombre
                return self.processeur_stock


    def ajoutCarteGrpahique(self):
        GPU = input("quelle marque de carte graphique voulez vous ajouter > ")
        if GPU != "":
            nbGPU = int(input("combien en voulez vous"))
            a = CarteGraphique(nbGPU, GPU)
            if GPU in self.carteGraphique_stock:
                composantsEnStock = self.carteGraphique_stock[GPU]
                nombre = a.nombre + composantsEnStock
                self.carteGraphique_stock.update({a.marque: nombre})
                return self.carteGraphique_stock
            else:
                self.carteGraphique_stock[a.marque] = a.nombre
                return self.carteGraphique_stock

    def ajoutHDD(self):
        HDD = input("quelle marque de HDD voulez vous ajouter > ")
        if HDD != "":
            nbHDD = int(input("combien en voulez vous"))
            a = HDD(nbHDD, HDD)
            if HDD in self.hdd_stock:
                composantsEnStock = self.hdd_stock[HDD]
                nombre = a.nombre + composantsEnStock
                self.hdd_stock.update({a.marque: nombre})
                return self.hdd_stock
            else:
                self.hdd_stock[a.marque] = a.nombre
                return self.hdd_stock

    def ajoutRAM(self):
        RAM = input("quelle marque de RAM voulez vous ajouter > ")
        if RAM != "":
            nbRAM = int(input("combien en voulez vous"))
            a = RAM(nbRAM, RRAM)
            if RAM in self.ram_stock:
                composantsEnStock = self.ram_stock[RAM]
                nombre = a.nombre + composantsEnStock
                self.ram_stock.update({a.marque: nombre})
                return self.ram_stock
            else:
                self.processeur_stock[a.marque] = a.nombre
                return self.processeur_stock

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
            print("\n1 - ajout processeur")
            print("2 - ajout carte graphique")
            print("3 - ajout hdd")
            print("4 - ajout RAM")
            composant = input("> ")

            if composant == "1":
                S.ajoutProcesseur()

            elif composant == "2":
                S.ajoutCarteGrpahique()

            elif composant == "3":
                S.ajoutHDD()

            elif composant == "4":
                S.ajoutRAM()

            else:
                pass


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
