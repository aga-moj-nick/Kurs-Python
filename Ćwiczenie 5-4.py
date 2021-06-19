wynik = 0
i = 0

while i < 3:
    a = int (input ("Podaj dodatnią liczbę parzystą: "))
    if (a > 0) and (a % 2 == 0):
        wynik += a
        i += 1

    else:
        print ("To nie jest liczba parzysta dodatnia. Trzeba powtórzyć!")
    continue

print ("Aktualny wynik dodawania to: ", wynik)