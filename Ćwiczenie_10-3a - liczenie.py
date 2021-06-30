# Ćwiczenie 10-2a - liczenie
"""
# ROZWIĄZANIE 1

def sumowanie_liczb (n):
    w = 0
    i = 0
    while i <= n:
        w += i
        i += 1
    return w

print (w)

# ROZWIĄZANIE 2

def sumowanie_liczb2 (n):
    w = 0
    for i in range (1, n + 1):
        w += i
    return w

print (w)

