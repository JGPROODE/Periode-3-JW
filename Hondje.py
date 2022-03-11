class Hondje():

    def __init__(self, mijnnaam,leeftijd):
        self.name = mijnnaam
        self.leeftijd = leeftijd

    def __str__(self):
        return("Deze Hond heet {} en is {} jaar oud.".format(self.name, self.leeftijd))

    def blaf(self):
       print("woeff")

hond1 = Hondje('kiky',18)
hond2 = Hondje('sysu',4)
hond3 = Hondje('fyfy',20)

print(hond1)
print(hond2)
print(hond3)