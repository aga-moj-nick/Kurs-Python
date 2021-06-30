# Ćwiczenie 10-2 - liczenie

# ROZWIĄZANIE 1
n = int (input ("Podaj wybraną liczbę: "))
i = 0
w = 0

while i <= n:
    w += i
    i += 1

print ("Wynik dodawania to: ", w)


# ROZWIĄZANIE 2
n = int (input ("Podaj wybraną liczbę: "))
w = 0

for i in range (0, n):
    w += i

print ("Wynik dodawania to: ", w)


# ROZWIĄZANIE 3
def sumowanie_liczb (n):
    return sum(range(1, n +1))

n = int (input ("Podaj wybraną liczbę n: "))
print ("Wynik dodawania to: ", sum(range(1, n +1)))


# ROZWIĄZANIE 3A
n = int (input ("Podaj wybraną liczbę n: "))
print ("Wynik dodawania to: ", sum(range(1, n +1)))


# ROZWIĄZANIE 4
def sumowanie_liczb (n):
    return (1 + n) / 2 * n

n = int (input ("Podaj wybraną liczbę n: "))
print ("Wynik dodawania to: ", sumowanie_liczb (n))
