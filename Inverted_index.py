import os
import glob
import dict_op
import pickle

Dictionaries = {}

filecount=0
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
               wordcount = wordcount + 1
               if (word != ""):
                    Dictionaries = dict_op.addDict(Dictionaries, word, filecount)
          #print alist
          filecount = filecount + 1;
          #print Dictionaries
     except:
          print "Something error!"
     finally:
          file_object.close()
#print Dictionaries
dict_file = open("inverted_dict", "wb")
pickle.dump(Dictionaries, dict_file)
dict_file.close()
