# ĆWICZENIE 8-3 - WYRAŻENIA SŁOWNIKOWE

names = {"Anna", "Elżbieta", "Małgorzata", "Ewa", "Magda", "Katarzyna", "Marta", "Agnieszka", "Joanna", "Aleksandra"}
numbers = {1, 2, 3, 4, 5, 6}
celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}



names_lenght = {
                name : len (name)
                for name in names
               }


names_lenght2 = {
                name : len (name)
                for name in names
                if name.startswith ("A")
                }


action_numbers = {
                  number : number + 10
                  for number in numbers
                 }


action_numbers2 = {
                  number : number - 5  
                  for number in numbers
                  }


action_numbers3 = {
                  number : number * 8
                  for number in numbers
                  }


action_numbers4 = {
                  number : number ** number
                  for number in numbers
                  }


action_numbers5 = {
                  number : number / 3
                  for number in numbers
                  }


action_numbers6 = {
                  number : number + number
                  for number in numbers
                  if number % 2 == 0
                  }


farenheit = {
            key : celcius * 1.8 + 32
            for key, celcius in celcius.items ()
            }


farenheit2 = {
             key : celcius * 1.8 + 32
             for key, celcius in celcius.items ()
             if celcius > -5
             }


farenheit3 = {
             key : celcius * 1.8 + 32
             for key, celcius in celcius.items ()
             if celcius > -5
             if celcius < 20
             }
