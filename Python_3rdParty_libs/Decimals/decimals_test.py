__author__ = 'k22li'


#case 1:  floating-point numbers calculations can't accurately represent all base-10 decimals

a = 2.1
b = 4.2
print a+b # which expecting 6.3 as the results, but because of the underlying CPU and the IEEE arithmetic performed by
# its floating-point unit.
# ACTUAL RESULT:  6.30000000000001
print a+b == 6.3 # False as the actual results because of the gaps as mentioned above


# Solutions:  importing the Decimal modules for decimal calculations.
from decimal import Decimal
a = Decimal('2.1')
b = Decimal('4.2')

print a+b

print type(a+b)

print (a+b) == Decimal('6.3')