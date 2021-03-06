# import dictionary
# for fn in glob.glob('Reuters/' + os.sep + '*.html'):
#    print fn

from dictionary import *
from corrector import *
from vsm import *
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
    global myvsm
    mydicts = Dictionary()
    pydict = PyDictionary()
    mydicts.read_compress("test1", "test2", "test3")
    myvsm = VSM(mydicts.count, mydicts.dict_in)

def search_vsm(word_str):
    global mydicts
    global pydict
    global myvsm

    word_list = []
    word_list_co = []
    word_list_ori = []

    word_list_ori = word_str.split(' ')
    for word in word_list_ori:
        if word in stopset:
            continue
        for item in deleteset:
            word = word.replace(item, '')
        if word == "":
            continue
        word_list.append(word)
        word_list_co.append(correct(word))


	file_id1 = []
	file_id2 = []
    file_id1 = myvsm.getTopK(word_list, 20)
    file_id2 = myvsm.getTopK(word_list_co, 20)

    strlist = []
    if(len(file_id2)-len(file_id1) > 10):
        for item in file_id2:
            if item == -1:
                continue
            fn = mydicts.file_id_record[item]

            try:
                file_object = open(fn)
                all_the_text = file_object.read()
                strlist.append((fn, all_the_text[0:200].replace("&lt;", "<")))
            except:
                print fn
            finally:
                file_object.close()
        return (1, strlist)
    else:
        for item in file_id1:
            if item == -1:
                continue
            fn = mydicts.file_id_record[item]

            try:
                file_object = open(fn)
                all_the_text = file_object.read()
                strlist.append((fn, all_the_text[0:200].replace("&lt;", "<")))
            except:
                print fn
            finally:
                file_object.close()
        return (0, strlist)


def search_inv_final(similar_tag, strand, strall, stror, strnot):
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
        if similar_tag == '1':
            for item in pydict.synonym(word):
                or_list.append(str(item))
                or_list_co.append(str(item))

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
        if (newstr!=""):
            and_list.append(newstr)
        if (newstr_co != ""):
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

        if similar_tag == "1":
            for item in pydict.synonym(word):
                or_list.append(str(item))
                or_list_co.append(str(item))

    for word in not_list_ori:
        if word in stopset:
            continue
        for item in deleteset:
            word = word.replace(item, '')
        if word == "":
            continue
        not_list.append(word)
        not_list_co.append(correct(word))

    print "length of or list:"
    print len(or_list)

    file_id1 = mydicts.search_invert(and_list, or_list, not_list)
    file_id2 = mydicts.search_invert(and_list_co, or_list_co, not_list_co)

    # for fn in glob.glob('../Reuters/' + os.sep + '*.html'):
    # print and_list, or_list, not_list
    # print and_list_co, or_list_co, not_list_co
    # print file_id1
    # print file_id2
    strlist = []
    if(len(file_id2)-len(file_id1) > 10):
        for item in file_id2:
            fn = mydicts.file_id_record[item]

            try:
                file_object = open(fn)
                all_the_text = file_object.read()
                strlist.append((fn, all_the_text[0:200].replace("&lt;", "<")))
            except:
                print fn
            finally:
                file_object.close()
        return (1, strlist)
    else:
        for item in file_id1:
            fn = mydicts.file_id_record[item]

            try:
                file_object = open(fn)
                all_the_text = file_object.read()
                strlist.append((fn, all_the_text[0:200].replace("&lt;", "<")))
            except:
                print fn
            finally:
                file_object.close()
        return (0, strlist)


# print f("apple")
# mydicts.read("test.txt")
# print (mydicts.mychange(8385))
