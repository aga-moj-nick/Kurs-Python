import figury_objetosci

wynik = input ("""Figury:
1. sześcian
2. prostopadłościan
3. graniastosłup
Podaj numer figury, której objętość chcesz obliczyć: """)


if (wynik == "1"):
    a = float (input ("Podaj a: "))
    print ("Objętość szcześcianu to: ", figury_objetosci.objetosc_szczescianu (a))

elif (wynik == "2"):
    a = float (input ("Podaj a: "))
    b = float (input ("Podaj b: "))
    H = float (input ("Podaj H: "))
    print ("Objętość prostopadłościanu to: ", figury_objetosci.objetosc_prostopadloscianu (a, b, H))

elif (wynik == "3"):
    Pp = float (input ("Podaj Pp: "))
    H = float (input ("Podaj H: "))
    print ("Objętość prostopadłościanu to: ", figury_objetosci.objetosc_graniastoslupa (Pp, H))

else:
    print ("Nie ma takiego numeru. Spróbuj jeszcze raz!")
