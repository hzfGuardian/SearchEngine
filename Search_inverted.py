from dictionary import *

mydicts = Dictionary("inverted_dict")

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








