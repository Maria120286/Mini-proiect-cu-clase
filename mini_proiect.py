from abc import ABC, abstractmethod


class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError


class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print('Copii invata sa deseneze.')

    def ora_de_somn(self):
        print('Copii trebuie sa doarma la ora 5.')


class GradinitaPrivata(Gradinita,
                       ABC):  # acesta este o clasa abstracta pentru ca nu defineste cele doua metode din clasa gradinita
    # la randul ei va deveni o clasa abstracta
    def activitate_practica(self):
        print('Copii invata sa modeleze cu plastelina.')


class GradinitaPublica25(GradinitaPublica):
    numar_elevi = 100
    _adresa = 'str Pacii ,nr30'
    __fonduri = 20000

    @property
    def fonduri(self):
        return self.__fonduri

    @fonduri.setter
    def fonduri(self, value):
        self.__fonduri = value

    @fonduri.deleter
    def fonduri(self):
        self.__fonduri = None

    def activitate_practica(self):
        print('Copii se joaca in curte pe balansoar.')

    def calculeaza_medie_buline_copii(self, buline):
        medie = sum(buline) / len(buline)
        if medie > 5:
            print('elevii acestey gradinite sunt foarte neastamparati')

    def infoElevi(self):
        elevi = {}
        while True:
            nume_elevi = input('introdu numele elevului :')
            nume_parinti = input('Introdu numele parintilor :')
            varsta = input('Varsta: ')
            activitate = input('introdu activitatea preferata :')
            elevi[nume_elevi] = {
                'Nume parinti: ': nume_parinti,
                'Varsta': varsta,
                'Activitatea:': activitate
            }
            introducere = input('Doresti sa introduceti date in continuare ? y/n')
            if introducere.lower() != 'y':
                break
        print(elevi)


p25 = GradinitaPublica25()
p25.activitate_practica()
p25.ora_de_somn()
p = GradinitaPublica()
p.activitate_practica()
# pr = GradinitaPrivata()
# pr.activitate_practica()
# polimorfism
p25.calculeaza_medie_buline_copii([1, 2, 3, 4, 5, 6, 7, 8, 9, 18])
print(p25.fonduri)
p25.fonduri = 25000
print(p25.fonduri)
del p25.fonduri
print(p25.fonduri)
p25.infoElevi()
