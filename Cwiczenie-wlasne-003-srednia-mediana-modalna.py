import math
from statistics import mode, median


oceny = {
    'polski': (5, 4, 4.5, 3, 4),
    'angielski': (5, 5, 4.5, 3.5, 4),
    'matematyka': (6, 5, 4.5, 3, 2, 5, 5),
    'biologia': (5.5, 6, 4.5, 6, 6)
    }


# Średnia arytmetyczna
def średnia_arytmetyczna (oceny):
    for key in oceny:
        return sum (oceny ['polski'])/len (oceny ['polski'])
print ('Oceny z polskiego to: ', oceny ['polski'])
print ('Średnia artytmetyczna z poslkiego to: ', średnia_arytmetyczna (oceny))

def średnia_arytmetyczna (oceny):
    for key in oceny:
        return sum (oceny ['angielski'])/len (oceny ['angielski'])
print ('Oceny z angielskiego to: ', oceny ['angielski'])
print ('Średnia artytmetyczna z angielskiego to: ', średnia_arytmetyczna (oceny))

def średnia_arytmetyczna (oceny):
    for key in oceny:
        return sum (oceny ['matematyka'])/len (oceny ['matematyka'])
print ('Oceny z matematyki to: ', oceny ['matematyka'])
print ('Średnia artytmetyczna z matematyki to: ', średnia_arytmetyczna (oceny))

def średnia_arytmetyczna (oceny):
    for key in oceny:
        return sum (oceny ['biologia'])/len (oceny ['biologia'])
print ('Oceny z biologii to: ', oceny ['biologia'])
print ('Średnia artytmetyczna z biologii to: ', średnia_arytmetyczna (oceny))


# Mediana:
def mediana (oceny):
    for key in oceny:
        return median (oceny ['polski'])
print ('Oceny z polskiego to: ', oceny ['polski'])
print ("Mediana ocen z polskiego to: ", mediana (oceny))

def mediana (oceny):
    for key in oceny:
        return median (oceny ['angielski'])
print ('Oceny z angielskiego to: ', oceny ['angielski'])
print ("Mediana ocen z angielskiego to: ", mediana (oceny))

def mediana (oceny):
    for key in oceny:
        return median (oceny ['matematyka'])
print ('Oceny z matematyki to: ', oceny ['matematyka'])
print ("Mediana ocen z matematyki to: ", mediana (oceny))

def mediana (oceny):
    for key in oceny:
        return median (oceny ['biologia'])
print ('Oceny z biologii to: ', oceny ['biologia'])
print ("Mediana ocen z biologii to: ", mediana (oceny))


# Modalna:
def modalna (oceny):
    for key in oceny:
        return mode (oceny ['polski'])
print ('Oceny z polskiego to: ', oceny ['polski'])
print ("Modalna ocen z polskiego to: ", modalna (oceny))

def modalna (oceny):
    for key in oceny:
        return mode (oceny ['angielski'])
print ('Oceny z angielskiego to: ', oceny ['angielski'])
print ("Modalna ocen z angielskiego to: ", modalna (oceny))

def modalna (oceny):
    for key in oceny:
        return mode (oceny ['matematyka'])
print ('Oceny z matematyki to: ', oceny ['matematyka'])
print ("Modalna ocen z matematyki to: ", modalna (oceny))

def modalna (oceny):
    for key in oceny:
        return mode (oceny ['biologia'])
print ('Oceny z biologii to: ', oceny ['biologia'])
print ("Modalna ocen z biologii to: ", modalna (oceny))


