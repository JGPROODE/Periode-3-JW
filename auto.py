#auto
#demo JGP Roode 10-2-2022

#Class definition
class Auto:
    def __init__(self, mijnkleur,mijnmerk):
        self.kleur=mijnkleur
        self.merk=mijnmerk

    def __str__(self):
        return("merk is : "+self.merk+" in de kleur :  "+self.kleur)


    def set_kleur(self, kleur):
        self.kleur=kleur

    def get_kleur(self):
        return self.kleur

    def geefGas(self):
        print('broemmmmmmmm')


auto1 =Auto("wit","Ford")

print(auto1)
print(auto1.get_kleur())
auto1.set_kleur("oranje")
print(auto1.get_kleur())

auto2=Auto('rood', 'toyota')
auto1.set_kleur('groen')
auto3=Auto('geel','fordt')

wagenpark=[auto1,auto2]
wagenpark.append(auto3)



for kar in wagenpark:
    print(kar)
    karretje.geefGas()
   # karretje.geefGas()