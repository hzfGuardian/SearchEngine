import pickle

# inverted index table


class Dictionary:
    dict_in = {}

    # load inverted index from disk
    def read(self, file_name):
        try:
            fin = open(file_name, "rb")
            self.dict_in = pickle.load(fin)
        finally:
            fin.close()

    def write(self, file_name):
        try:
            fin = open(file_name, "wb")
            pickle.dump(self.dict_in, file_name)
        finally:
            fin.close()

    # [[2, [1, 2, 6, 7]], [3, [3, 4]]] : [[doc_id1, [pos1, ...]], [doc_id2, [pos1, ...]]]
    def addItem(self, item, doc_id, pos):
        if item in self.dict_in:  # item found
            for node in self.dict_in[item]:
                if doc_id == node[0]:  # [2, [1, 2, 6, 7]]
                    i = self.dict_in[item].index(node)
                    if pos not in node[1]:
                        self.dict_in[item][i][1] += [pos]
                    return
            self.dict_in[item] += [[doc_id, [pos]]]
        else:
            new_dict = {item: [[doc_id, [pos]]]}
            self.dict_in.update(new_dict)

    def serchaword(self, word):
        result = []
        if (len(word.split(' ')) < 2):
            if word not in self.dict_in:
                return result
            for myitem in self.dict_in[word]:
                result.append(myitem[0])
            return result
        else:
            word_list=word.split(' ')
            index = 0
            temp = []
            result = []
            for word in word_list:
                if word not in self.dict_in:
                    return result

            for word in word_list:
                if (index==0):
                    temp = self.dict_in[word]
                    index = index + 1
                    continue
                temp2 = self.dict_in[word]
                result_temp = []
                flag=0
                for olditem in temp:
                    for newitem in temp2:
                        if (olditem[0] == newitem[0]):
                            for inta in olditem[1]:
                                for intb in newitem[1]:
                                    if(intb-inta==index):
                                        result_temp.append(newitem[0])
                                        break
                                else:
                                    continue
                                break
                            else:
                                continue
                            break
                if(index == 1):
                    result = result_temp
                else:
                    result = list(set(result).intersection(set(result_temp)))
                index = index + 1
            return result