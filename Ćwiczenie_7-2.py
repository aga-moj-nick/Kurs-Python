# Dynamiczny słownik z definicjami

slownik = {}


while (True):
    
    print ("\n", "D: dodaj definicję", "\n", "S: szukaj definicji", "\n", "U: usuń definicję", "\n", "Z: zakończ", "\n")

    uzytkownik = input ("Wybierz odpowiednią literkę: ")



    if (uzytkownik.upper () == "D"):
        haslo = input ("Podaj hasło: ")
        definicja = input ("Podaj definicję: ")
        slownik [haslo] = definicja
        print ("Hasło i definicja zostały dodane do słownika: ", "\n", "'", haslo.capitalize () , "-" , slownik [haslo], "'", sep="")

    elif (uzytkownik.upper () == "S"):
        haslo = input ("Podaj poszukiwane hasło: ")
        if haslo in slownik:
            print ("Definicja do Twojego hasła to: ", "'", haslo.capitalize (), " ", "-", " ", slownik [haslo], "'", sep="")
        else:
            print ("W słowniku nie ma takiego hasła.")

    elif (uzytkownik.upper () == "U"):
        haslo = input ("Podaj hasło, które chcesz usunąć: ")
        if haslo in slownik:
            del slownik [haslo]
            print ("Hasło zostało usunięte ze słownika.")
        else:
            print ("W słowniku nie ma takiego hasła.")
        
    elif (uzytkownik.upper () == "Z"):
        print ("Praca ze słownikiem została zakończona.")
        break

    else:
        print ("Nie ma takiej literki. Spróbuj jeszcze raz.")
