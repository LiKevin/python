# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
#   with...as.. to implement the AOP
# fixme: Python的with...as...子句是用于控制执行流程的语句，结构是with expression as variable，
# fixme: 这里的expression里定义拦截的方法前后需要执行的逻辑，
# fixme: 分别定义“__enter__”和“__exit__”方法，“__enter__”方法定义拦截方法执行前的逻辑，
# fixme: “__exit__”方法定义拦截方法执行后的逻辑，with...as...子句的主体是拦截的方法执行的逻辑，
# fixme: variable变量是用来接收“__enter__”方法返回的值
# fixme: while issubclass() methods working with parent & super parent class as well
#######################################################################################################################

# demo 1
#######################################################################################################################
class test:

    def __enter__(self):
        print('>>> enter processing started...')
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>> exit processing started...')


def function_to_aop():
    print('>>> function() to execute...')
    return 111

with test() as t:       #fixme:  with子句中的variable接收的是__enter__方法的返回值。这是with子句的基本用法.
    function_to_aop()
    print('t is: %s'%t)
