import dictionary
#for fn in glob.glob('Reuters/' + os.sep + '*.html'):
 #    print fn
from dictionary import *
mydicts = Dictionary()
mydicts.read("test.txt")
print (mydicts.search_invert(["apple"], [], []))