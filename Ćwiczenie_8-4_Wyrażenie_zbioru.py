# Ćwiczenie_8-4_Wyrażenie_zbioru

names = {"Anna", "Elżbieta", "małgorzata", "Ewa", "Magda", "katarzyna", "Marta", "agnieszka", "joanna", "aleksandra"}

names = {
         name.capitalize ()
         for name in names
        }


names1 = {
         name
         for name in names
         if name [0] != "A"
        }
