import random
from enum import Enum

Drzwi = Enum ('Drzwi', ['Białe_Drzwi', 'Czarne_Drzwi'])

słownik_drzwi = {Drzwi.Białe_Drzwi: 0.4,
                 Drzwi.Czarne_Drzwi: 0.6
                 }

lista_drzwi = tuple (słownik_drzwi.keys ())
prawdopodobieństwo_drzwi = tuple (słownik_drzwi.values ())



Kule = Enum ('Kule', {'Platyna': 'platynowa',
                     'Złoto': 'złota',
                     'Srebro': 'srebrna'}
            )


słownik_kul = {'Platyna': 0.05,
               'Złoto': 0.15,
               'Srebro': 0.8
              }


lista_kul = tuple (słownik_kul.keys ())
prawdopodobieństwo_kul = tuple (słownik_kul.values ())


piętra = 3

print ("Jesteś w Tajemniczym Zamku. Aby dojść do wieży, musisz pokonać trzy magiczne piętra. Na każdym otworzą się przed Tobą drzwi - białe lub czarne. Co Cię spotka za nimi? Przekonaj się sam!")


while piętra > 0:
    gracz = input ("Czy chcesz iść na górę? ")
    if gracz == 'tak':
        print ("Zaraz zobaczysz drzwi!")
        zobaczone_drzwi = random.choices (lista_drzwi, prawdopodobieństwo_drzwi) [0]
        print ("Przed Tobą pojawiają się: ", zobaczone_drzwi)
        if zobaczone_drzwi == Drzwi.Białe_Drzwi:
            print ("Wygrałeś jedną z trzech kul!")
            wylosowany_kolor_kuli = random.choices (lista_kul, prawdopodobieństwo_kul) [0]
            print ("Kolor wygranej kuli to: ", wylosowany_kolor_kuli)
        if zobaczone_drzwi == Drzwi.Czarne_Drzwi:
            print ("Brak kul. Może na kolejnym piętrze będzie lepiej")
    else:
        print ("Nie to nie. Koniec gry")
        break

    piętra -= 1
























    
