# -*- coding: utf-8 -*-

"""
闭包(closure)是函数式编程的重要的语法结构。函数式编程是一种编程范式 (而面向过程编程和面向对象编程也都是编程范式)。
在面向过程编程中，我们见到过函数(function)；在面向对象编程中，我们见过对象(object)。
函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)。
闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。不同的语言实现闭包的方式不同。
Python以函数对象为基础，为闭多包这一语法结构提供支持的 (我们在特殊方法与多范式中，已经次看到Python使用对象来实现一些特殊的语法)。
Python一切皆对象，函数这一语法结构也是一个对象。在函数对象中，我们像使用一个普通对象一样使用函数对象，比如更改函数对象的名字，或者将函数对象作为参数进行传递。
"""

#example 1 (Closure, 闭包)

def line_conf():

    def line(x):
        return 2*x+1

    return line #return the func itself to the main call


#example 2 (Closure, 闭包)
"""
我们可以看到，line定义的隶属程序块中引用了高层级的变量b，但b信息存在于line的定义之外 (b的定义并不在line的隶属程序块中)。我们称b为line的环境变量。
事实上，line作为line_conf的返回值时，line中已经包括b的取值(尽管b并不隶属于line)。

下面的代码将打印25，也就是说，line所参照的b值是函数对象定义时可供参考的b值，而不是使用时的b值。
"""
def line_conf2():

    b = 15
    def line2(x):
        return 2*x + b #local param will be used, instead of the global params

    return line2


#example 3 (__closure__)
"""
一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中。
"""


#example 4
def line_conf3(a, b):

    def line3(x):
        return a*x+b

    return line3

"""
这个例子中，函数line与环境变量a,b构成闭包。在创建闭包的时候，我们通过line_conf的参数a,b说明了这两个环境变量的取值，这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)。
我们只需要变换参数a,b，就可以获得不同的直线表达函数。由此，我们可以看到，闭包也具有提高代码可复用性的作用。
"""



if __name__ == '__main__':

    b = 30
    testFunc = line_conf2()
    for i in range(2, 5):
        print testFunc(i)
    print testFunc.__closure__[0].cell_contents #the value of "b" inside the closure

    testFunc3 = line_conf3(2, 4)
    print testFunc3(3)
    print testFunc3(5)

    testFunc4 = line_conf3(4, 5)
    print testFunc4(6)

"""
如果没有闭包，我们需要每次创建直线函数的时候同时说明a,b,x。这样，我们就需要更多的参数传递，也减少了代码的可移植性。利用闭包，我们实际上创建了泛函。
line函数定义一种广泛意义的函数。
这个函数的一些方面已经确定(必须是直线)，但另一些方面(比如a和b参数待定)。随后，我们根据line_conf传递来的参数，通过闭包的形式，将最终函数确定下来。
"""