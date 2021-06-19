# ćwiczenie "jak masz na imię?"
print ("Jak masz na imię?")
imie = input ()
print ("Hej ", imie.capitalize (), ",", " jak masz na nazwisko?", sep= "")
nazwisko = input ()
print (imie.capitalize () + " " + nazwisko.capitalize (), ",", " ile masz lat?", sep= "")
wiek = int (input () )
print ("Za rok będziesz mieć", (wiek + 1))
print ("Jakie jest Twoje hobby ", imie.capitalize (), "?", sep="")
hobby = input ()
print (hobby.upper (), "jest super!", "Miłego dnia :)")



