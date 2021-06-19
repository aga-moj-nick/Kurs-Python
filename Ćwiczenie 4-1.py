wybor = input ("* - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie, ** - potęgowanie, % - modulo: ")

a = int (input ("Pierwsza liczba to: "))
b = int (input ("Druga liczba to: "))


if (wybor == "*"):
    print (a * b)

elif (wybor == "/") :
    if (b == 0) :
        print ("Nie dziel przez 0!!!")
    else :
        print (a / b)

elif (wybor == "+") :
    print (a + b)


elif (wybor == "-") :
    print (a - b)

elif (wybor == "**") :
    print (a ** b)

elif (wybor == "%") :
    print (a % b)