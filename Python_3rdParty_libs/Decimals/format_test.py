__author__ = 'k22li'
#format is a built-in functions from Python

# case 1:

a = 1234.56789

#^ stands for center justified displaying with the 10 digits length
# , stands for displaying of the 'Inclusions of thousands separator
# 2f stands for reserving the 2 digits after the
print format(a, '^10,.2f'), len(str(a))

# < stands for left justified displaying of 10 digits as the outputs
print format(a, '<10,.2f'), len(str(a))

#> stands for right justified displaying of the 10 digits as the outputs
print format(a, '>10,.2f'), len(str(a))



#fractions.Fraction

from fractions import Fraction

print Fraction(5, 4) # 5/4

print Fraction(6, 4) # 3/2


a = Fraction(5, 4)
b = Fraction(7, 16)

print a+b
c = a*b

print 'c.numerator: %s; c.denominator: %s'%(c.numerator, c.denominator)

