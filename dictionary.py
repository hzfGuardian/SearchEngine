import pickle


# inverted index table

class Dictionary:
    dict_in = {}
    file_name = ""

    # load inverted index from disk
    def read(self, file_name):
        self.file_name = file_name
        try:
            fin = open(file_name, "rb")
            self.dict_in = pickle.load(fin)
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

