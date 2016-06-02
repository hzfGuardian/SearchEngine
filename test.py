

file_object = open('1.html')
try:
     all_the_text = file_object.read();
     print all_the_text;
finally:
     file_object.close();
