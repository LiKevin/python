# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
2.函数入参数为一个二维数组，比如3*7的一个二维数组，数组元素值表示一种颜色，一共5种颜色，同一个颜色上下左右，不包括斜方向，
可以连成一个国家，比如A[0][0],A[0][1]组成一个国家，A[0]1[],A[0][2]，A[1][2]颜色为3，组成一个国家，函数返回二维数组表示国家的个数。
1，3，3，
1，2，3，
2，4，5，
。。。。
要求一定的时间和空间复杂度，不只是完成就可以。
'''
def get_all_coordinates(lst):
    '''
    get & store each elements coordinates into a dict
    '''
    results_dict = {}
    x = -1
    for outter_lst in lst:
        x += 1
        y=-1
        for elem in outter_lst:
            y += 1
            if results_dict.has_key(elem):
                results_dict[elem].append((x,y))
            else:
                results_dict.update({elem: [(x, y)]})

    return results_dict

def analyze_related_coordinates_fixed(lst=[]):
    '''
    walk through a coordinates list, and figure out the relative coordinates and count for the isolated \
    coordinates numbers
    '''
    if not lst:
        return 0

    # get the full list size
    length = len(lst)
    # for storing the numbers of the related coordinates to the 1st, 2nd, 3rd ... etc elements
    relative_elem_numbers = []
    counter = 0
    while 1:
        if lst:
            elem = lst.pop(0)
            x0, y0 = elem
            for item in lst:
                x1, y1 = item
                if abs(x0-x1)+abs(y0-y1)== 1:  #break,once there is a relative item available from the rest of the list
                    break
            else:
                relative_elem_numbers.append(elem) # recording the item so long as there isn't any relative ones
        else:
            break
    return len(relative_elem_numbers)

def get_country_numbers(dct={}):
    '''
    return the lists which stores the country numbers
    '''
    return [[key_elem, analyze_related_coordinates_fixed(dct[key_elem])] for key_elem in dct]

def main(lst):
    '''
    the main function to do the calculations
    '''
    coordinates = get_all_coordinates(lst)
    return get_country_numbers(coordinates)

if __name__=='__main__':

    list_a = [[1,3,3],[1,2,3],[2,4,5],[2,3,4],[5,5,4],[2,3,4],[2,2,3]]
#    list_b = [[1,3,1], [2,2,2], [3,3,3],[3,3,3],[3,3,3]]
    list_c = [[3,3,3],[3,3,3],[3,3,3],[3,3,3],[3,3,3]]
    print main(list_c)
