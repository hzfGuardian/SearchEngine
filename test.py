
from dictionary import *

mydicts = Dictionary()

mydicts.addItem('a', 1, 3)

print mydicts.dict_in

mydicts.addItem('a', 2, 2)

print mydicts.dict_in

mydicts.addItem('b', 2, 2)

print mydicts.dict_in

print mydicts.serchaword('b')

#mydicts.write("inverted_dict")


word_and_list = {"a", "b"}
word_or_list = {"sb", "apple"}
word_not_list = {"add", "b"}
Resule_id = []

stopset = {"is", "a", "he", "she", "and", "are", "am", "of", "for", "were", "in", "it", "them", "its", "would", "share", "The"}
for i in stopset:
    stopset.remove(i)
print stopset


