'''
def add(a, b):
     return a+b

try:
     file_object = open('2.html')
     all_the_text = file_object.read()
     print all_the_text
except:
     print '2'
finally:
     print '3'
     file_object.close()

'''
import pickle
f2 = open("inverted_dict", "rb")
load_list = pickle.load(f2)
f2.close()
# print
print load_list


