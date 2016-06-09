# import dictionary
# for fn in glob.glob('Reuters/' + os.sep + '*.html'):
#    print fn

from dictionary import *

mydicts = Dictionary()


def search_inv_init():
    global mydicts
    mydicts = Dictionary()
    mydicts.read_compress("test1", "test2")


def search_inv_final(strand, strall, stror, strnot):
    global mydicts
    add_list = []
    or_list = []
    not_list = []
    

    resule_id = mydicts.search_invert(add_list, or_list, not_list)
    return resule_id

# print f("apple")
# mydicts.read("test.txt")
# print (mydicts.mychange(8385))
