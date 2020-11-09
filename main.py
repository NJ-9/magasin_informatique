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
            self.carteGraphique_stock[a.marque] = a.nombre
            return self.carteGraphique_stock

    def ajoutHDD(self):
        HDD = input("quelle marque de HDD voulez vous ajouter > ")
        if HDD != "":
            nbHDD = int(input("combien en voulez vous"))
            a = HDD(nbHDD, HDD)
            self.hdd_stock[a.marque] = a.nombre
            return self.hdd_stock

    def ajoutRAM(self):
        RAM = input("quelle marque de RAM voulez vous ajouter > ")
        if RAM != "":
            nbRAM = int(input("combien en voulez vous"))
            a = RAM(nbRAM, RRAM)
            self.ram_stock[a.marque] = a.nombre
            return self.ram_stock

    def affichierStock(self):
        print("\nprocesseur : ", self.processeur_stock)
        print("carte graphique : ", self.carteGraphique_stock)
        print("hdd : ", self.hdd_stock)
        print("ram : ", self.ram_stock, '\n')

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
            pass

        else:
            break
