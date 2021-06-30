from enum import Enum

Menu_Dni_Tygodnia = Enum ("Menu_Dni_Tygodnia", "Poniedziałek Wtorek Środa Czwartek Piątek Sobota Niedziela")

uzytkownik = int(input ("""Wybierz ulubiony dzień tygodnia:
1. Poniedziałek,
2. Wtorek,
3. Środa,
4. Czwartek,
5. Piątek,
6. Sobota,
7. Niedziela.
Podaj odpowiednią cyferkę: """))

if uzytkownik == Menu_Dni_Tygodnia.Poniedziałek.value:
    print ("Pierwszy dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Wtorek.value:
    print ("Drugi dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Środa.value:
    print ("Trzeci dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Czwartek.value:
    print ("Czwarty dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Piątek.value:
    print ("Piąty dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Sobota.value:
    print ("Szósty dzień tygodnia")

elif uzytkownik == Menu_Dni_Tygodnia.Niedziela.value:
    print ("Siódmy dzień tygodnia")

else:
    print ("Zły wybór!")

