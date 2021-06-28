# Ćwiczenie_9-1 

ksiazki = ["sf", "kryminał", "romans"]

def czytam (ksiazka):
    print ("Zazwyczaj czytam: ", ksiazka, ";)")

for ksiazka in ksiazki:
    czytam (ksiazka)



owoce = ["truskawki", "czereśnie", "banany", "jabłka", "gruszki"]

def lista_zakupow (owoc):
    print ("Na liście zakupów mam: ", owoc, ", bo lubię je najbardziej!", "Są super!", sep='')

for owoc in owoce:
    lista_zakupow (owoc)
