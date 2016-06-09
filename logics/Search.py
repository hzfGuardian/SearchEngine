# import dictionary
# for fn in glob.glob('Reuters/' + os.sep + '*.html'):
#    print fn

from dictionary import *
from corrector import *
from PyDictionary import PyDictionary

mydicts = Dictionary()

pydict = PyDictionary()


stopset = {"is", "a", "he", "she", "and", "are", "am", "of", "for", "were", "in", "it", "them", "its", "would", "share",
           "The", "an", "him", "her", "what", "be", "now", "good", "I'm", "No", "not", "It", "TO", "about", "also",
           "as", "at", "been", "but", "by", "from", "had", "has", "have", "last", "on", "one", "or", "said", "that",
           "the", "this", "to", "up", "vs", "was", "which", "will", "with", "I"}
deleteset= {'\n', '\r', '>', '<', ')', '(', '\"', "\'", '&lt', '-', '+', '@', '%', '^', '*', ':', ';', '&amp'}

def search_inv_init():
    global mydicts
    global pydict
    mydicts = Dictionary()
    pydict = PyDictionary()
    mydicts.read_compress("test1", "test2", "test3")


def search_inv_final(strand, strall, stror, strnot):
    global mydicts
    global pydict
    and_list_ori = strand.split(' ')
    or_list_ori = stror.split(' ')
    not_list_ori = strnot.split(' ')
    all_list_ori = strall.split(',')
    and_list = []
    or_list = []
    not_list = []
    and_list_co = []
    or_list_co = []
    not_list_co = []
    for word in and_list_ori:
        if word in stopset:
            continue
        for item in deleteset:
            word = word.replace(item, '')
        if word == "":
            continue
        and_list.append(word)
        and_list_co.append(correct(word))
        #for item in pydict.synonym(word):
         #   or_list.append(str(item))
          #  or_list_co.append(str(item))

    for item in all_list_ori:
        newstr = ""
        newstr_co = ""
        templist=item.split(' ')
        flag = 0
        for word in templist:
            if word in stopset:
                continue
            for item in deleteset:
                word = word.replace(item, '')
            if word == "":
                continue
            if flag == 0:
                flag = flag + 1
                newstr = word
                newstr_co = correct(word)
            else:
                newstr = newstr + " " + word
                newstr_co = newstr_co + " " + correct(word)
        and_list.append(newstr)
        and_list_co.append(correct(newstr_co))

    for word in or_list_ori:
        if word in stopset:
            continue
        for item in deleteset:
            word = word.replace(item, '')
        if word == "":
            continue
        or_list.append(word)
        or_list_co.append(correct(word))
        #for item in pydict.synonym(word):
         #   or_list.append(str(item))
          #  or_list_co.append(str(item))

    for word in not_list_ori:
        if word in stopset:
            continue
        for item in deleteset:
            word = word.replace(item, '')
        if word == "":
            continue
        not_list.append(word)
        not_list_co.append(correct(word))

    file_id1 = mydicts.search_invert(and_list, or_list, not_list)
    file_id2 = mydicts.search_invert(and_list_co, or_list_co, not_list_co)

   # for fn in glob.glob('../Reuters/' + os.sep + '*.html'):

    strlist = []
    if(len(file_id2)-len(file_id1) > 10):
        for item in file_id2:
            fn = mydicts.file_id_record[item]

            try:
                file_object = open(fn)
                all_the_text = file_object.read()
                strlist.append((fn, all_the_text[0:100]))
            except:
                print fn
            finally:
                file_object.close()
        return (1,strlist)
    else:
        for item in file_id1:
            fn = mydicts.file_id_record[item]

            try:
                file_object = open(fn)
                all_the_text = file_object.read()
                strlist.append((fn, all_the_text[0:100]))
            except:
                print fn
            finally:
                file_object.close()
        return (0, strlist)


# print f("apple")
# mydicts.read("test.txt")
# print (mydicts.mychange(8385))
