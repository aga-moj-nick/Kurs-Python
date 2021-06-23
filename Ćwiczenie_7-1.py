# 36. WPISYWANIE ZAWARTOŚCI SŁOWNIKA ZAGNIEŻDŻONEGO W LIŚCIE/SŁOWNIKU - ćWICZENIE

people1 = {
            "abc": {'name': 'Adam', 'surname': 'Kowalski', 'age': 27, 'sex': 'Male', 'school_class': 'A'},
            "cde": {'name': 'Maria', 'surname': 'Nowak', 'age': 22, 'sex': 'Female', 'school_class': 'B'},
            "efg": {'name': 'Agnieszka', 'surname': 'Malinowska', 'age': 25, 'sex': 'Female', 'school_class': 'A'},
            "ghi": {'name': 'Norbert', 'surname': 'Wisniewski', 'age': 17, 'sex': 'Male', 'school_class': 'C'},
            "ijk": {'name': 'Janina', 'surname': 'Adamiak', 'age': 42, 'sex': 'Female', 'school_class': 'A'},
            "klm": {'name': 'Rozalia', 'surname': 'Maj', 'age': 55, 'sex': 'Female', 'school_class': 'A'},
            "mno": {'name': 'Tomasz', 'surname': 'Michalak', 'age': 27, 'sex': 'Male', 'school_class': 'C'},
            "opr": {'name': 'Maria', 'surname': 'Cegielska', 'age': 42, 'sex': 'Female', 'school_class': 'B'},
            "rst": {'name': 'Anna', 'surname': 'Czarnecka', 'age': 25, 'sex': 'Female', 'school_class': 'C'},
            "tuw": {'name': 'Cezary', 'surname': 'Szewczyk', 'age': 17, 'sex': 'Male', 'school_class': 'A'},
            "wyz": {'name': 'Martyna', 'surname': 'Marciniak', 'age': 2, 'sex': 'Female', 'school_class': 'B'},
         }


people2 = [
           {id: 'abc', 'name': 'Jan', 'age': 27, 'sex': 'Male'},
           {id: 'cde', 'name': 'Maria', 'age': 22, 'sex': 'Female'},
           {id: 'efg', 'name': 'Anna', 'age': 25, 'sex': 'Female'},
          ]

people3 = ["Adam",
           "Wiola",
           "Karol"
            ]


ratings1 = {
     "Adam": (1, 2, 3, 4, 5, 6),
     "Dominika": (5, 6, 5, 4, 5, 6)
     }


"""
Ćwiczenie - wypisać zawartość dla
1. people3 +
2. raitings1 +
3. people2 +
4. people1


# RATINGS1

for key in ratings1:
    print (key)

for key in ratings1:
    print (ratings1 [key])

for key in ratings1:
    print (key, ":", "oceny", ratings1 [key])


# PEOPLE1

print (people1)

for id in people1:
    print (id)


for id, dictionary in people1:
    print ("ID:", id)
    for key in dictionary:
        print (key, ":", dictionary [key])

for key in people1:
    print ("\n", "ID:", key)
    for secondary_key in people1 [key]:
        print (secondary_key, people1 [key] [secondary_key])


print (people1.items ())

for key in people1.items ():
    print ("\n", "ID:", key)

for id, dictionary in people1.items ():
    print ("\n", id)

for id, dictionary in people1.items ():
    print ("\n", dictionary)

for id, dictionary in people1.items ():
    print ("\n", id, dictionary)


# PEOPLE2

for value in people2:
    print (value)

for dictionary in people2:
    for key in dictionary:
        print (key, ":", dictionary [key])


# PEOPLE3

for value in people3:
    print (value)
"""












    
