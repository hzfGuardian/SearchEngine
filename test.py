
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


