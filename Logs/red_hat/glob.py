import glob
#
#for x in glob.iglob("./*.py"):
#    print ">>> python files: %s" %x


print dir(glob.glob)
print glob.glob(r"../*.py")
