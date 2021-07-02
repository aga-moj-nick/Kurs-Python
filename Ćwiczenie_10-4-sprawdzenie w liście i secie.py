# 55. ĆWICZENIE - SPRAWDZANIE, CZY ISTNIEJE ELEMENT WEWNĄTRZ ZBIORU VS LISTY


import time


set_kontener = {i for i in range (0, 50)}
list_kontener = [i for i in range (0, 15)]


def sprawdzanie (wartość):
    if wartość in set_kontener:
        return True
    else:
        return False
      

def sprawdzanie2 (wartość):
    if wartość in list_kontener:
        return True
    else:
        return False


print (sprawdzanie (30))
print (sprawdzanie2 (30))


def function_performence (funkc, arg, how_many_times = 1):
    sum = 0
    for i in range (0, how_many_times):
        start = time.perf_counter ()
        funkc (arg)
        end = time.perf_counter ()
        sum = sum + (end - start)
        
    return sum

print (function_performence (sprawdzanie, 30, how_many_times = 1000))
print (function_performence (sprawdzanie2, 30, how_many_times = 1000))
