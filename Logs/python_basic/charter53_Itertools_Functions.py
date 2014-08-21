# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
#   is to demo the functions built-in the itertools modules
#
#    3.4. 相关的库
#    Python内置了一个模块itertools，包含了很多函数用于creating iterators for efficient looping（创建更有效率的循环迭代器），
#    这说明很是霸气，这一小节就来浏览一遍这些函数并留下印象吧，需要这些功能的时候隐约记得这里面有就好。
#    这一小节的内容翻译自itertools模块官方文档。
#
#    fixme: 3.4.1. 无限迭代
#    count(start, [step])
#    从start开始，以后每个元素都加上step。step默认值为1。
#    count(10) --> 10 11 12 13 14 ...
#    cycle(p)
#    迭代至序列p的最后一个元素后，从p的第一个元素重新开始。
#    cycle('ABCD') --> A B C D A B C D ...
#    repeat(elem [,n])
#    将elem重复n次。如果不指定n，则无限重复。
#    repeat(10, 3) --> 10 10 10
#
#    fixme: 3.4.2. 在最短的序列参数终止时停止迭代
#    chain(p, q, ...)
#    迭代至序列p的最后一个元素后，从q的第一个元素开始，直到所有序列终止。
#    chain('ABC', 'DEF') --> A B C D E F
#    compress(data, selectors)
#    如果bool(selectors[n])为True，则next()返回data[n]，否则跳过data[n]。
#    compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
#    dropwhile(pred, seq)
#    当pred对seq[n]的调用返回False时才开始迭代。
#    dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
#    takewhile(pred, seq)
#    dropwhile的相反版本。
#    takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
#    ifilter(pred, seq)
#    内建函数filter的迭代器版本。
#    ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
#    ifilterfalse(pred, seq)
#    ifilter的相反版本。
#    ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
#    imap(func, p, q, ...)
#    内建函数map的迭代器版本。
#    imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
#    starmap(func, seq)
#    将seq的每个元素以变长参数(*args)的形式调用func。
#    starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
#    izip(p, q, ...)
#    内建函数zip的迭代器版本。
#    izip('ABCD', 'xy') --> Ax By
#    izip_longest(p, q, ..., fillvalue=None)
#    izip的取最长序列的版本，短序列将填入fillvalue。
#    izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
#    tee(it, n)
#    返回n个迭代器it的复制迭代器。
#    groupby(iterable[, keyfunc])
#    这个函数功能类似于SQL的分组。使用groupby前，首先需要使用相同的keyfunc对iterable进行排序，比如调用内建的sorted函数。然后，groupby返回迭代器，每次迭代的元素是元组(key值, iterable中具有相同key值的元素的集合的子迭代器)。或许看看Python的排序指南对理解这个函数有帮助。
#    groupby([0, 0, 0, 1, 1, 1, 2, 2, 2]) --> (0, (0 0 0)) (1, (1 1 1)) (2, (2 2 2))
#
#    fixme: 3.4.3. 组合迭代器
#    fixme: product(p, q, ... [repeat=1])
#    笛卡尔积。
#    product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
#    fixme: permutations(p[, r])
#    去除重复的元素。
#    permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#    fixme: combinations(p, r)
#    排序后去除重复的元素。
#    combinations('ABCD', 2) --> AB AC AD BC BD CD
#    combinations_with_replacement()
#    排序后，包含重复元素。
#    fixme: combinations_with_replacement('ABCD', 2) --> AA AB AC AD BB BC BD CC CD DD
########################################################################################################################

import itertools

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##3.4.1. 无限迭代##
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# demo 1:  count(start, [step]): 从start开始，以后每个元素都加上step。step默认值为1。
########################################################################################################################
counter = itertools.count(10, step=2)

def _test_count():
    for i in range(20):
        print counter.next()


# demo 2:  cycle([]): 迭代至序列p的最后一个元素后，从p的第一个元素重新开始。
########################################################################################################################
cycler = itertools.cycle(['a', 'b', 'c'])

def _test_cycle():
    for i in range(5):
        print cycler.next()

# demo 3: repeat(elem, [n,]):  将elem重复n次。如果不指定n，则无限重复。
########################################################################################################################
repeater = itertools.repeat('kevin', 20)

def _test_repeat():
    try:
        for i in range(21):
            print repeater.next()
    except StopIteration, err:
        pass


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##3.4.2. 在最短的序列参数终止时停止迭代##
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# demo 1: chain(p, q ...): 迭代至序列p的最后一个元素后，从q的第一个元素开始，直到所有序列终止。
########################################################################################################################
p_list = ['a', 'b', 'c']
q_tuple = ('e', 'f')

def _test_chain():

    for item in itertools.chain(p_list, q_tuple):
        print item

# demo 2: compress(data, selectors): 如果bool(selectors[n])为True，则next()返回data[n]，否则跳过data[n]。
# e.g: compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
########################################################################################################################
data = 'abcdefg'
selecter = [i % 2==0 and 1 or 0 for i in range(7)]

def _test_compress():
    for item in itertools.compress(data, selecter):
        print item


# demo 3: dropwhile(pred, seq): fixme: 当pred对seq[n]的调用返回False时才开始迭代  区分与map，单一条件判断
# e.g: dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
########################################################################################################################
pred = lambda x: x%2==0
seq = range(10)

def _test_dropwhile():
    for item in itertools.dropwhile(lambda x:x%3==0, seq):
        print item

    # outputs: "1, 2, 3, 4, 5, 6, 7, 8 ,9"

# demo 4: takewhile(pred, seq): fixme: 当pred对seq[n]的调用返回False时才开始迭代  区分与map，单一条件判断
# e.g: takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
########################################################################################################################
def _test_takewhile():
    for item in itertools.takewhile(pred, seq):
        print item

    # outputs：  "0"

#    others:
#    fixme: ifilter(pred, seq)
#    内建函数filter的迭代器版本。
#    ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
#    fixme: ifilterfalse(pred, seq)
#    ifilter的相反版本。
#    ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
#    fixme: imap(func, p, q, ...)
#    内建函数map的迭代器版本。
#    imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
#    fixme: starmap(func, seq)
#    将seq的每个元素以变长参数(*args)的形式调用func。
#    starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
#    fixme: izip(p, q, ...)
#    内建函数zip的迭代器版本。
#    fixme: izip('ABCD', 'xy') --> Ax By
#    fixme: izip_longest(p, q, ..., fillvalue=None)
#    izip的取最长序列的版本，短序列将填入fillvalue。
#    izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
#    fixme: tee(it, n)
#    返回n个迭代器it的复制迭代器。
#    fixme: groupby(iterable[, keyfunc])
#    这个函数功能类似于SQL的分组。使用groupby前，首先需要使用相同的keyfunc对iterable进行排序，比如调用内建的sorted函数。然后，groupby返回迭代器，每次迭代的元素是元组(key值, iterable中具有相同key值的元素的集合的子迭代器)。或许看看Python的排序指南对理解这个函数有帮助。
#    groupby([0, 0, 0, 1, 1, 1, 2, 2, 2]) --> (0, (0 0 0)) (1, (1 1 1)) (2, (2 2 2))

########################################################################################################################
# test codes
########################################################################################################################

if __name__ == '__main__':

#    _test_repeat()

#    _test_chain()

#    _test_compress()

#    _test_dropwhile()

    _test_takewhile()