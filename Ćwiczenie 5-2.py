mojKolor = str ("czerwony")
kolorZagadka = " "


while kolorZagadka != mojKolor:
    kolorZagadka = str (input ("Odgadnij kolor: "))

    if (kolorZagadka != mojKolor):
        print ("To nie ten kolor!")

    else:
        print ("Brawo!")