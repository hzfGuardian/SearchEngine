import os
import glob
from dictionary import *

mydicts = Dictionary()
filecount = 0
stopset = {"is", "a", "he", "she", "and", "are", "am", "of", "for", "were", "in", "it", "them", "its", "would", "share", "The"}
for fn in glob.glob('Reuters/' + os.sep + '*.html'):
     #print fn
     try:
          file_object = open(fn)
          all_the_text = file_object.read()
          #print all_the_text
          alist=all_the_text.split(' ')
          #data_list = list(jieba.cut(all_the_text))
          wordcount = 0
          for word in alist:
               word = word.strip()
               word = word.strip(",")
               word = word.rstrip(">")
               word = word.rstrip(".")
               word = word.lstrip("/'")
               word = word.lstrip('/"')
               word = word.rstrip("/'")
               word = word.rstrip('/"')
               word = word.strip("&lt;")
               if (word != "" and word not in stopset):
                    mydicts.addItem(word, filecount, wordcount)
                    wordcount = wordcount + 1
          #print alist
          filecount = filecount + 1;
          #print Dictionaries
     except:
          print "Something error!"
     finally:
          file_object.close()
#print Dictionaries
#mydicts.sortDict()
#mydicts.write("inverted_dict")
#mydicts.addItem('a', 1, 3)
word_and_list = {"a", "b"}
word_or_list = {"sb", "apple"}
word_not_list = {"add", "b"}

Resule_id = []
count_op = 0
for word_and in word_and_list:
    if count_op == 0:
        Resule_id = mydicts.serchaword(word_and)  # wait for new things
    else:
        Resule_id = list(set(Resule_id).intersection(set(mydicts.serchaword(word_and))))  # must change
    if(len(Resule_id) == 0):
        break
    count_op = count_op + 1

for word_or in word_or_list:
    if count_op == 0:
        Resule_id = mydicts.serchaword(word_or)  # wait for new things
    else:
        Resule_id = list(set(Resule_id).union(set(mydicts.serchaword(word_or))))  # must change
    count_op = count_op + 1

for word_not in word_not_list:
    if count_op != 0:
        Resule_id = list(set(Resule_id).difference(set(mydicts.serchaword(word_not))))  # must change
        count_op = count_op + 1

print Resule_id