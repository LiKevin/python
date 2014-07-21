#-*- utf-8 -*-
__author__ = 'k22li'

# reverse a strings
str_1 = 'i miss you now'

class stringReserving():

    """
    reverse the strings per given
    """

    def reverseStringsViaConvertingToList(string1):
        """
        reverse the strings provided via converting to list
        """
        str_1_list = string1.split()
        str_1_list.reverse()
        str_2 = " ".join(str_1_list)
        return str_2


    def reverseStringsViaConvertingToSet(string2):
        """
        find out the unique letters, and join them together
        """
        str1_set = set(string2)
        str2_list = list(str1_set)

        return ''.join(str2_list)



#t = reverseStringsViaConvertingToSet(str_1)
#print t
class HelperFunction():

    def __init__(self, className):
        print '*'*78
        return help(className)


if __name__ == '__main__':

    HelperDescriptor = HelperFunction(stringReserving)