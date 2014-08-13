# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
#    python中eval, exec, execfile,和compile
#    分类： python 2011-10-31 15:34 918人阅读 评论(0) 收藏 举报
#    pythonlambdac2010
#    此日志为转载，原文链接：http://skandgjxa.blog.163.com/blog/static/1415298201010262403483/
#
#    eval(str [,globals [,locals ]])函数将字符串str当成有效Python表
#
#    达式来求值，并返回计算结果。
#
#    同样地, exec语句将字符串str当成有效Python代码来执行.提供给exec的代码的名称空间和exec语句的名称空间相同.
#
#    最后，execfile(filename [,globals [,locals ]])函数可以用来执行一个文件,看下面的例子:
#
#    >>> eval('3+4')
#    7
#    >>> exec 'a=100'
#    >>> a
#    100
#    >>> execfile(r'c:\test.py')
#    hello,world!
#    >>>
#    默认的，eval(),exec,execfile()所运行的代码都位于当前的名字空间中. eval(), exec,和 execfile()函数也可以接受一个或两个
#
#    可选字典参数作为代码执行的全局名字空间和局部名字空间. 例如:
#
#    切換行號
#    1 globals = {'x': 7,
#                 'y': 10,
#                 'birds': ['Parrot', 'Swallow', 'Albatross']
#                }
#    locals = { }
#
#    #fixme: 将上边的字典作为全局和局部名称空间
#    fixme: a = eval("3*x + 4*y", globals, locals)
#    fixme: exec "for b in birds: print b" in globals, locals   # 注意这里的语法
#    fixme: execfile("foo.py", globals, locals)
#
#    如果你省略了一个或者两个名称空间参数,那么当前的全局和局部名称空间就被使用.如果一个函数体内嵌嵌套函数或lambda匿名函数
#    时,同时又在函数主体中使用exec或execfile()函数时， 由于牵到嵌套作用域，会引发一个SyntaxError异常.
#    fixme: 注意例子中exec语句的用法和eval(),execfile()是不一样的.exec是一个语句(就象print或while),而eval()和execfile()则是内
#    建函数.
#
#    exec(str) 这种形式也被接受，但是它没有返回值。 --WeiZhong
#    fixme: 当一个字符串被exec,eval(),或execfile()执行时,解释器会先将它们编译为字节代码，然后再执行.这个过程比较耗时,所以如果需要
#    fixme: 对某段代码执行很多次时,最好还是对该代码先进行预编译,这样就不需要每次都编译一遍代码，可以有效提高程序的执行效率。
#    fixme: compile(str ,filename ,kind )函数将一个字符串编译为字节代码, str是将要被编译的字符串, filename是定义该字符串变量
#    fixme: 的文件，kind参数指定了代码被编译的类型-- 'single'指单个语句, 'exec'指多个语句, 'eval'指一个表达式.
#    fixme: cmpile()函数返回一个代码对象，该对象当然也可以被传递给eval()函数和exec语句来执行,例如:
#    str = "for i in range(0,10): print i"
#    fixme: c = compile(str,'','exec')      #fixme: 编译为字节代码对象
#    fixme: exec c                          #fixme: 执行
#
#    str2 = "3*x + 4*y"
#    fixme: c2 = compile(str2, '', 'eval')   #fixme: 编译为表达式
#    fixme: result = eval(c2)               #fixme: 执行
########################################################################################################################

# demo 1
########################################################################################################################
t = compile('a + b', '', 'eval')
p = eval(t, {'a': 4, 'b': 5}) # eval has return values, and possible to assign to a variable;
print p

# demo 2
########################################################################################################################
t2 = compile('print a + b', '', 'exec') # if you want to print the result, has to invoke print method here
#p2  = exec(t2)
exec(t2, {}, {'a': 4, 'b': 5})    # exec has NOT return values, and impossible to assign to a variable;