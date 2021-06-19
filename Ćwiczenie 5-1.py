# Ćwiczenie "zgadnij liczbę"


mojaCyfra = 5
cyfraZagadka = 0

while cyfraZagadka != mojaCyfra:
    cyfraZagadka = int (input ("Odgadnij cyfrę: "))

    if (cyfraZagadka > mojaCyfra):
        print ("Za dużo!")

    elif (cyfraZagadka < mojaCyfra):
        print ("Za mało!")

    else:
       print ("Brawo!")