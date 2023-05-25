# Import Build-in modules in Python
import math
import math,random ## importing two modules at once
import random as Edna # import with renaming modules
from math import factorial # import specific functions from a module (the from statement)
print(math.sqrt(9))
print(math.log(10))
print(math.factorial(5))
print(math.factorial(5), random.randint(20, 30)) # this imports two modules at a time
print(random.randint(23, 37)) # example of importing two modules at once ('randint' is a function in the 'random' module)

# importing power function
base=20
exponent=5
print(math.pow(20,5))

print(Edna.randint(10, 30)) # import with renaming modules

from math import sqrt as Drizzle
print(Drizzle(2)) #is correct cos math is already defined and Drizzle replaces sqrt
