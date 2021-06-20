studenci = {101:["Anna", "Kowalska", "polonistyka"],
            102:["Zdzichu", "Nowak", "matematyka"],
            103:["Krzysztof", "Maliniak", "pedagogika"]}



uzytkownik = ""

while uzytkownik.upper () != "Q":

    uzytkownik = input ("Naciśnij W, jeśli chcesz wyświelić listę uczestników wycieczki lub Q jeśli chcesz zakończyć: ")

    if uzytkownik.upper () == "Q":
        break
    
    if uzytkownik.upper () == "W":
        for i in studenci:
            print(i, studenci[i]) 
        
        zmiany = input ("Naciśnij D, jeśli chcesz dodać nowego studenta lub U, jeśli chcesz usunąć: ")
        
        if zmiany.upper () == "D":
            lista_tymczasowa = []
            id = int (input ("Podaj id: ")) 
            if id in studenci:
                print ("Podane id już istnieje. Spróbuj jeszcze raz")
                continue
            
            imie = input ("Podaj imię: ")
            nazwisko = input ("Podaj nazwisko: ")
            kierunek = input ("Podaj kierunek studiów: ")
            lista_tymczasowa.append (imie)
            lista_tymczasowa.append (nazwisko)
            lista_tymczasowa.append (kierunek)
            studenci.update({id:lista_tymczasowa})

        if zmiany.upper() == "U":
            usun_id = int (input ("Podaj id do skasowania: "))
            studenci.pop (usun_id)
            
            


