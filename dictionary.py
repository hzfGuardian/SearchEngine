#import pickle
import os
import glob
import struct
# inverted index table

class Dictionary:
    dict_in = {}
    count = 0

    # load inverted index from disk
    def read(self, file_name):
        try:
            fin = open(file_name, "r")
            #self.dict_in = pickle.load(fin)
            len_dic = int(fin.readline())
            self.count = int(fin.readline())
            for i in range(0, len_dic):
                word = fin.readline()
                word = word.rstrip("\n")
                word = word.rstrip("\r")
                len_file = int(fin.readline())
                word_list = []
                if(len_file > 1000):
                   print("\""+word+"\",")
                for j in range(0, len_file):
                    pos_list= []
                    file_id = int(fin.readline())
                    len_pos = int(fin.readline())
                    for k in range(0, len_pos):
                        a = int(fin.readline())
                        pos_list.append(a)
                    word_list.append([file_id, pos_list])
                self.dict_in[word] = word_list
        except Exception, e:
            print e
        finally:
            fin.close()

    def write(self, file_name):
        try:
            fout = open(file_name, "w")
            #pickle.dump(self.dict_in, file_name)
            dic_list = self.sortdict()
            fout.write(str(len(dic_list)))
            fout.write("\r\n")
            fout.write(str(self.count))
            fout.write("\r\n")
            for item in dic_list:
                fout.write(item[0])
                fout.write("\r\n")
                fout.write(str(len(item[1])))
                fout.write("\r\n")
                for docid in item[1]:
                    fout.write(str(docid[0]))
                    fout.write("\r\n")
                    fout.write(str(len(docid[1])))
                    fout.write("\r\n")
                    for pos in docid[1]:
                        fout.write(str(pos))
                        fout.write("\r\n")
        finally:
            fout.close()

    def mychange(self,number):
        return 1

    def write_compress(self, word_file_name, index_file_name):
        try:
            wordfile = open(word_file_name, "wb")
            indexfile = open(index_file_name, "wb")
            dic_list = self.sortdict()
            wordfile.write(self.mychange(len(dic_list)))




        finally:
            wordfile.close()
            indexfile.close()

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

    def sortdict(self):
        return sorted(self.dict_in.iteritems(), key=lambda asd: asd[0])

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

    def search_invert(self, word_and_list, word_or_list, word_not_list):
        Resule_id = []
        count_op = 0
        for word_and in word_and_list:
            if count_op == 0:
                Resule_id = self.serchaword(word_and)  # wait for new things
            else:
                Resule_id = list(set(Resule_id).intersection(set(self.serchaword(word_and))))  # must change
            if (len(Resule_id) == 0):
                break
            count_op = count_op + 1

        for word_or in word_or_list:
            if count_op == 0:
                Resule_id = self.serchaword(word_or)  # wait for new things
            else:
                Resule_id = list(set(Resule_id).union(set(self.serchaword(word_or))))  # must change
            count_op = count_op + 1

        for word_not in word_not_list:
            if count_op != 0:
                Resule_id = list(set(Resule_id).difference(set(self.serchaword(word_not))))  # must change
                count_op = count_op + 1
        return Resule_id