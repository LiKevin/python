# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# 0-1 背包
#
# 有N件物品和一个容量为m的背包。第i件物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使价值总和最大。
########################################################################################################################


weights = [c[i] for i in range(N)]
values= [w[i] for i in range(N)]

goods ={weight1: value1, weight2: value2}
m = 30

def dp_cases():
    total_weights = 0
    for weight in goods.keys():
        if total_weights <= m:
            total_weights += weight
            total_values += goods[weight]