__author__ = 'k22li'

def fxrange(start, stop, increment):

    x = start
    while x < stop:
        yield x
        x += increment

def printf(comment):
    t = len(comment)
    if t < 100:
        print '*'*((100-t)/2), '%s' %(comment),'*'*((100-t)/2)
    else:
        print '*'*5, '%s' %(comment),'*'*5

# display all those iters via For LOOPs
#print '*'*30, '%s' %('display all iters via for() looping'),'*'*30

printf('display all iters via for() looping')
for i in fxrange(0, 4, 0.5):
    print i

# display each of those iters via next() calling
printf('display each of the iter via Next() calling')
print fxrange(0, 4, 1).next()

# display all those iters via list methods
printf('display all of those iters via List() methods')
a = list(fxrange(0, 10, 1))
print a