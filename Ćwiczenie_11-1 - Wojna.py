import random

talia = ["9", "9", "9", "9",
         "10", "10", "10","10",
         "Jack",  "Jack",  "Jack",  "Jack",
         "Queen", "Queen", "Queen", "Queen",
         "King", "King", "King","King",
         "Ace", "Ace", "Ace", "Ace",
         "Joker", "Joker"]

gracz1 = []
gracz2 = []

def rozdanie (gracz1, gracz2):
    random.shuffle (talia)
    i = 0
    while i < 5:
        rozdane_karty = talia.pop ()
        gracz1.append (rozdane_karty)
        rozdane_karty = talia.pop ()
        gracz2.append (rozdane_karty)
        i += 1
    return gracz1, gracz2

print (rozdanie (gracz1, gracz2))






