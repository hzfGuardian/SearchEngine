# import dictionary
# for fn in glob.glob('Reuters/' + os.sep + '*.html'):
#    print fn

from dictionary import *


def f(word):
    mydicts = Dictionary()
    mydicts.read_compress("test1", "test2")
    word = mydicts.search_invert([word], [], [])
    return word

# print f("apple")
# mydicts.read("test.txt")
# print (mydicts.mychange(8385))
