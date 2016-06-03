import pickle

file = open("inverted_dict", "rb")
load_list = pickle.load(file)
file.close()

def searchphrase(phrase):
    result = []
    if (len(phrase.split(' ')) < 2):
        return result

word_and_list = {"a", "said"}
word_or_list = {"sb", "apple"}
word_not_list = {"add", "set"}
Resule_id = []

count_op = 0
for word_and in word_and_list:
    if word_and in load_list:
        if count_op == 0:
            Resule_id = load_list[word_and]  # wait for new things
        else:
            Resule_id = list(set(Resule_id).intersection(set(load_list[word_and])))  # must change
        if(len(Resule_id) == 0):
            break
    count_op = count_op + 1

for word_or in word_or_list:
    if word_or in load_list:
        if count_op == 0:
            Resule_id = load_list[word_and]  # wait for new things
        else:
            Resule_id = list(set(Resule_id).union(set(load_list[word_and])))  # must change
    count_op = count_op + 1

for word_not in word_not_list:
    if word_not in load_list:
        if count_op != 0:
            Resule_id = list(set(Resule_id).difference(set(load_list[word_and])))  # must change
    count_op = count_op + 1

print Resule_id








