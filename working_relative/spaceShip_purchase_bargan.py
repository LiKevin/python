__author__ = 'k22li'


def checkio(data):

    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data

    gap = initial_oldman-initial_sofi
    print gap

    if gap%(raise_sofi+reduction_oldman) == 0:
        print gap/(raise_sofi+reduction_oldman)
        return initial_sofi+raise_sofi*gap/(raise_sofi+reduction_oldman)

    else:
        print gap/(raise_sofi+reduction_oldman)
        return initial_sofi+raise_sofi*(gap/(raise_sofi+reduction_oldman)+1)
    #replace this for solution
    return 0

#Some hints
#Be careful with endless loop


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    assert checkio([150, 50, 900, 100]) == 400, "2nd example"
