# -*- coding:  utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpoes:
# "if...else.. " logical implementations via "(... and ... or (... and ...or ( ...and ...or...))))"; 函数式编程
########################################################################################################################

# demo 1:  map
########################################################################################################################

expr = lambda airQuality: (( airQuality < 50) and '良好' or ((airQuality<100) and '中等' or ((airQuality < 150) \
          and '对敏感人群不健康' or ((airQuality < 200) and '差' or ((airQuality<300) and '非常差' or \
         '非常非常差，完全不建议户外活动')))))

# test code 1
def _test_map_lambda():
    k = map(expr, [39, 50, 160])
    for item in k:
        print item.decode('utf-8')


# demo 2:  filter
########################################################################################################################
expr2 = lambda airQuality: airQuality<150

# test code 2
def _test_filter_lambda():
    f = filter(expr2, [50, 39, 150])
    for item in f:
        print item

# demo 2:  reduce
########################################################################################################################
expr3 = lambda airQuality: airQuality<50

# test code 2
def _test_reduce_lambda():
    r = reduce(expr3, [150])

    print r

########################################################################################################################
# testing starts
########################################################################################################################

if __name__ == '__main__':
#    _test_filter_lambda()

    _test_reduce_lambda()