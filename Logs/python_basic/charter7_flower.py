__author__ = 'k22li'

for i in range(100,1000):
    a = i%10
    b = i%100//10
    c = i//100
    if a**3+b**3+c**3 == i:
        print(i)


z=[ [1,2] , [3,4] , [1,2] , [5,6] , [7,8] , [9,0] , [3,4] , [1,2] , [7,8] ]

print [ repr(list_item) for list_item in z]

#print type(eval('[1, 2]'))

zr = [repr(x) for x in z]


import sets

zs = sets.Set(zr)

print zs

zf = [eval(x) for x in zs]
print zf


dct = dict(enumerate(z))
try:
    print dict(zip(dct.values(), dct.keys()))

except TypeError as e:

    print 'Error: %s' %e