__author__ = 'k22li'


with open("../nst_mtbf.mini.libra_wk28.testplan", "r") as planHandler:

    planHandler.seek(0)
    line = planHandler.readline()
    print line, planHandler.tell(), len(line)

    planHandler.flush()
