# Ćwiczenie 8-2 Wyrażenia słownikowe

numbers = {1, 2, 3, 4, 5, 6}

action_numbers = {
                        number : number ** 2
                        for number in numbers
                         }


action_numbers1 = {
                       number : number + 10
                       for number in numbers
                         }


action_numbers2 = {
                        number : number - 5
                        for number in numbers
                          }


action_numbers3 = {
                        number : number / 2
                        for number in numbers
                          }


action_numbers4 = {
                        number : number * number
                        for number in numbers
                          }
