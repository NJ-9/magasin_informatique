class Stock:
    def __init__(self):
        self.processeur_stock = {}
        self.carteGraphique_stock = {}
        self.hdd_stock = {}
        self.ram_stock = {}


    def ajoutProcesseur(self, nombre, marque):
        a = Processeur(nombre, marque)
        self.processeur_stock[a.marque] = a.nombre
        return self.processeur_stock

    def ajoutCarteGrpahique(self, nombre, marque):
        a = CarteGraphique(nombre, marque)
        self.processeur_stock[a.marque] = a.nombre
        return self.processeur_stock

    def ajoutHDD(self, nombre, marque):
        a = HDD(nombre, marque)
        self.processeur_stock[a.marque] = a.nombre
        return self.processeur_stock

    def ajoutRAM(self, nombre, marque):
        a = RAM(nombre, marque)
        self.processeur_stock[a.marque] = a.nombre
        return self.processeur_stock



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
    print(S.ajoutProcesseur(5, "AMD"))
