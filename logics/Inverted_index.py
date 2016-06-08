import os
import glob
from dictionary import *

mydicts = Dictionary()
filecount = 0
stopset = {"is", "a", "he", "she", "and", "are", "am", "of", "for", "were", "in", "it", "them", "its", "would", "share",
           "The", "an", "him", "her", "what", "be", "now", "good", "I'm", "No", "not", "It", "TO", "about", "also",
           "as", "at", "been", "but", "by", "from", "had", "has", "have", "last", "on", "one", "or", "said", "that",
           "the", "this", "to", "up", "vs", "was", "which", "will", "with", "I"}
deleteset= {'\n', '\r', '>', '<', ')', '(', '\"', "\'", '&lt', '-', '+', '@', '%', '^', '*', ':', ';', '&amp'}
for fn in glob.glob('../Reuters/' + os.sep + '*.html'):
     #print fn
     try:
          file_object = open(fn)
          all_the_text = file_object.read()
          #print all_the_text
          alist=all_the_text.split(' ')
          #data_list = list(jieba.cut(all_the_text))
          wordcount = 0
          for word in alist:
               for item in deleteset:
                    word = word.replace(item, '')
               word = word.strip()
               word = word.strip(",")
               word = word.strip(".")
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

mydicts.count = filecount
#print Dictionaries
#mydicts.dict_in = sorted(mydicts.dict_in.iteritems(), key=lambda asd: asd[0])
#mydicts.write("inverted_dict")
#mydicts.addItem('a', 1, 3)
'''dic_list=mydicts.sortdict()
lon = len(dic_list)
lon2 = len(mydicts.dict_in)
for item in dic_list:
    a = item[0]
    b = item[1]
    c= len(b)
'''
mydicts.write_compress("test1", "test2")

#mydicts2 = Dictionary()
#mydicts2.read("test.txt")
