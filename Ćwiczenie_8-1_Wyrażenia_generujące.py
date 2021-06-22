# WYRAŻENIA GENERUJĄCE

import sys

even_generator_numbers = (element ** 2
                          for element in range (100))
                        

print (even_generator_numbers)
print (sys.getsizeof (even_generator_numbers))

for item in even_generator_numbers:
    print (item)

print (sum (even_generator_numbers))
