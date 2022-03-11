# class hond
class Hond():

    # constructor met attributen
    def __init__(self, naam, leeftijd, kleur):
        self.naam = naam
        self.leeftijd = leeftijd
        self.kleur = kleur

    # return value wanneer class 'hond' geprint wordt
    def __str__(self):
        return ("Deze hond heet: {}, is {} jaar oud en zijn kleur is {}.".format(self.naam, self.leeftijd, self.kleur))
    
    # functie om hond te laten blaffen
    def blaf(self):
        print('Woef!')


# honden aanmaken en 3 parameters meegeven
hond1 = Hond('Nick', 8, 'bruin')
hond2 = Hond('Django', 3, 'zwart')
hond3 = Hond('Burt', 5, 'snow-white')
hond4 = Hond('henkie',99,'blauw')

# een hondenkennel met drie honden
kennelhonden = [hond1, hond2, hond3]

#er komt een hond bij.
kennelhonden.append(Hond("Max",9,"bruin met vlekken"))

#alle honden uit de kennel afdrukken en laten blaffen
for hond in kennelhonden:
     print(hond)
     hond.blaf()
   
