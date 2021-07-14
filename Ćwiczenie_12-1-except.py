# Ćwiczenie 12-1

"""
ĆWICZENIE: FileNotFoundError exception
Stwórz funkcję, która obsługuje otwieranie pliku do wczytywania danych.

Zapytaj się użytkownika o nazwę pliku, który chce otworzyć do wczytania.

Jeśli plik nie istnieje wypisz mu odpowiedni komunikat.

Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji.

Podpowiedź: skorzystaj z wiedzy dotyczącej obsługi wyjątków z poprzedniej lekcji:

except FileNotFoundError:
"""



def odczytywanie (plik):
    try:
        with open (plik, "r", encoding = "UTF-8") as file:
            return file.read ()
    except FileNotFoundError:
        print ("Nie ma takiego pliku")


uzytkownik = input ("Podaj nazwę pliku: ")

print (odczytywanie (uzytkownik))
