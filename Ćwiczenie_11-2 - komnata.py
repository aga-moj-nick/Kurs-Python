import random
from enum import Enum

Event = Enum ('Event',['Skrzynia', 'Pusty'])

słownik_eventów = {Event.Skrzynia: 0.6,
                   Event.Pusty: 0.4}

lista_eventów = tuple (słownik_eventów.keys ())
prawdopodobieństwo_eventów = tuple (słownik_eventów.values ())

Kolory = Enum ('Kolory', {'Green': 'zielony',
                          'Orange': 'pomarańczowy',
                          'Purple': 'fioletowy',
                          'Gold': 'złoty'
                         }
               )

słownik_kolorów = {Kolory.Green: 0.75,
                   Kolory.Orange: 0.2,
                   Kolory.Purple: 0.04,
                   Kolory.Gold: 0.01
                  }

lista_kolorów = tuple (słownik_kolorów.keys ())
prawdopodobieństwo_kolorów = tuple (słownik_kolorów.values ())

nagrody_w_skrzyniach = {lista_kolorów [nagroda]: (nagroda +1) * (nagroda +1) * 1000
                        for nagroda in range (len (lista_kolorów))
                       }


ruchy = 5
zdobyte_złoto = 0

print ("""Witaj w Komnacie! Tu rozpocznie się przygoda Twojego życia!
        Masz tylko pięć ruchów, ale możesz zdobyć mnóstwo złota! Zatem do dzieła!
        """)

while ruchy > 0:
    gracz = input ("Czy chcesz iść do przodu? ")
    if (gracz == "tak"):
        print ("Zobaczmy, co otrzymałeś :)")
        wylosowany_event = random.choices (lista_eventów, prawdopodobieństwo_eventów)[0]
        print (wylosowany_event)
        if (wylosowany_event == Event.Skrzynia):
            print ("Wygrałeś skrzynię!")
            wylosowany_kolor_skrzyni = random.choices (lista_kolorów, prawdopodobieństwo_kolorów)[0]
            print ("Kolor Twojej skrzyni to: ", wylosowany_kolor_skrzyni.value)
            nagroda_gracza = nagrody_w_skrzyniach [wylosowany_kolor_skrzyni]
            zdobyte_złoto = zdobyte_złoto + nagroda_gracza 
        elif (wylosowany_event == Event.Pusty):
            print ("Nic nie wygrałeś!")
    else:
        print ("Możesz iść tylko do przodu")
        continue
    ruchy = ruchy - 1
    
print ("Gratulacje! Wygrałeś: ", zdobyte_złoto, "złota")
