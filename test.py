'''
def addDict(dictin, item, docID):
    if item in dictin:  # item found
        if docID not in dictin[item]:
            dictin[item] += [docID]
        return dictin

    new_dict = {item: [docID]}
    dictin.update(new_dict)  # = dict(dictin.items() + new_dict.items())
    return dictin

'''
import pickle
file = open("inverted_dict", "rb")
load_list = pickle.load(file)
file.close()

def searchphrase(phrase):
    result = []
    if ( len(phrase.split(' ')) < 2 ):
        return result



word_and_list = {"a", "said"}
word_or_list = {"sb", "apple"}
word_not_list = {"add", "set"}
Resule_id = []



# print
#print load_list







<<<<<<< HEAD
from dictionary import *

mydicts = Dictionary()
=======
>>>>>>> 19138345ecfebf518433f69990db9a299f981c6c

mydicts.addItem('a', 1, 3)

print mydicts.dict_in

mydicts.addItem('a', 1, 2)

print mydicts.dict_in

mydicts.addItem('a', 2, 2)

print mydicts.dict_in