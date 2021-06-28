from enum import IntEnum

Menu_Dni_Tygodnia = IntEnum ("Menu_Dni_Tygodnia", "Poniedziałek Wtorek Środa Czwartek Piątek Sobota Niedziela")

uzytkownik = int (input ("""Wybierz ulubiony dzień tygodnia:
1. Poniedziałek,
2. Wtorek,
3. Środa,
4. Czwartek,
5. Piątek,
6. Sobota,
7. Niedziela.
Podaj odpowiednią cyferkę: """))

if uzytkownik == Menu_Dni_Tygodnia.Poniedziałek:
    print ("Pierwszy dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Wtorek:
    print ("Drugi dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Środa:
    print ("Trzeci dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Czwartek:
    print ("Czwarty dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Piątek:
    print ("Piąty dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Sobota:
    print ("Szósty dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Niedziela:
    print ("Siódmy dzień tygodnia")

else:
    print ("Zły wybór!")
