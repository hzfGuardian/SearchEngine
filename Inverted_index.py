import os
import glob
import pickle
from dict_op import *

Dictionaries = {}

filecount = 0
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
               if (word != ""):
                    Dictionaries = addDict(Dictionaries, word, filecount, wordcount)
                    wordcount = wordcount + 1
          #print alist
          filecount = filecount + 1;
          #print Dictionaries
     except:
          print "Something error!"
     finally:
          file_object.close()
#print Dictionaries
Dictionaries = sorted(Dictionaries.iteritems(), key=lambda asd: asd[0])
dict_file = open("inverted_dict", "wb")
pickle.dump(Dictionaries, dict_file)
dict_file.close()
