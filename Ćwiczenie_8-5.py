# Ćwiczenie_8-5

"""
Znajdź liczby od 100 do 470 włącznie, które są:
- podzielne przez 7, ale nie są podzielne przez 5

Z czego skorzystasz?
1.	Generatora
2.	Wyrażenia listowego
3.	Wyrażenia zbioru
4.	Wyrażenia słownikowego?

Zastanów się, czy odpowiedź na to pytanie jest zawsze taka sama?
"""

"""
# GENERATOR
import sys 

numbers = [element
                for element in range (100, 471)
                if (element % 7 == 0) and (element % 5 != 0)
                ]


print (numbers)


# WYRAŻENIE LISTOWE

numbers =          [element
                   for element in range (100, 471)
                   if (element % 7 == 0) and (element % 5 != 0)]



# WYRAŻENIA ZBIORU

numbers = {
         number
         for number in range (100, 471)
         if (number % 7 == 0) and (number % 5 != 0)
        }
"""
