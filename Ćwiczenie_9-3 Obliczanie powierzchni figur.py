# Ćwiczenie_9-1 Obliczanie powierzchni figur

import math
"""
ĆWICZENIE: Program liczący powierzchnie figur
Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:

1) prostokąta

2) kwadratu

3) trójkąta

4) trapezu

5) koła

Pamiętaj, by skorzystać z funkcji.
"""

while (True):

    print ("Powierzchnia figur: 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło lub 6 - zakończ program")
    uzytkownik = int (input ("Wybierz odpowiednią cyferkę: "))


    def pole_prostokata (a, b):
        return (a * b)

    def pole_trojkata (a, h):
        return ((a / 2) * h)

    def pole_trapezu (a, b, h):
        return (((a + b) / 2 ) * h)

    def pole_kola (r):
        return (math.pi * math.pow(r, 2))


    if uzytkownik == 1 or uzytkownik == 2:
        bokA = int (input ("Podaj długość boku a: "))
        bokB = int (input ("Podaj długość boku b: "))
        print ("Pole prostokąta/kwadratu to: ", pole_prostokata (bokA, bokB))


    if uzytkownik == 3:
        bok = int (input ("Podaj długość boku: "))
        wysokosc = int (input ("Podaj wysokość: "))
        print ("Pole prostokąta/kwadratu to: ", pole_trojkata (bok, wysokosc))

    if uzytkownik == 4:
        bokA = int (input ("Podaj długość boku a: "))
        bokB = int (input ("Podaj długość boku b: "))
        wysokosc = int (input ("Podaj długość h: "))
        print ("Pole prostokąta/kwadratu to: ", pole_trapezu (bokA, bokB, wysokosc))

    if uzytkownik == 5:
        promien = int (input ("Podaj długość boku a: "))
        print ("Pole prostokąta/kwadratu to: ", pole_kola (promien))

    if uzytkownik == 6:
        break

    if uzytkownik <= 0 or uzytkownik > 6:
        print ("Zły wybór")

    
