import dictionary
#for fn in glob.glob('Reuters/' + os.sep + '*.html'):
 #    print fn

from dictionary import *
mydicts = Dictionary()
#mydicts.read("test.txt")
mydicts.read_compress("test1", "test2")
#print (mydicts.search_invert(["apply"], ["pear"], []))
a = 1
#print (mydicts.mychange(8385))
