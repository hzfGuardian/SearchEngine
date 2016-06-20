
from query import *
import math
import numpy as np
# import scipy as sp


class VSM:
    dos_len = 0
    matrix = np.zeros
    dic = {}
    sort_dic = {}   # record the sort id for each item

    def __init__(self, docs, dicts):
        self.dic = dicts
        self.dos_len = docs
        self.matrix = np.zeros((len(dicts), docs))
        dicts = sorted(dicts.iteritems(), key=lambda asd: asd[0])

        # create index
        self.sort_dic = self.createSortedDict(self.dic)

        # tf-idf
        for i in range(0, len(dicts)):  # for each item
            idf = math.log10(1.0 * docs / len(dicts[i]))  # calculate idf for each item

            for node in dicts[i][1]:
                doc_id = node[0]  # get docID
                tf = len(node[1])
                if tf > 0:
                    self.matrix[i, doc_id] = (1 + math.log10(tf * 1.0)) * idf
                else:
                    self.matrix[i, doc_id] = 0
        # print self.sort_dic
        return

    def createSortedDict(self, dicts):
        dic = {}

        # get all keys of dicts
        tmp_list = dicts.keys()

        # sort
        tmp_list.sort()

        for i in range(0, len(tmp_list)):
            dic[tmp_list[i]] = i

        # return the dict in form of {'apple': 0, 'boy': 1 ...}
        return dic

    def printMatrix(self):
        print self.matrix

    # transfer Query Object to query vector
    def qryVector(self, query):
        vq = np.zeros(len(self.dic))
        for item in query.and_items:
            if item in self.sort_dic:
                row_id = self.sort_dic[item]
                vq[row_id] = 1
        return vq

    def cosineScore(self, id_word_list, doc_id):
        valid_vd = []
        for item in id_word_list:
            valid_vd.append(self.matrix[item, doc_id])

        if np.linalg.norm(valid_vd) == 0 or len(id_word_list) == 0:
            return 0
        else:
            return np.linalg.norm(valid_vd, 1) / (np.linalg.norm(valid_vd, 2) * np.sqrt(len(id_word_list)))

    def getTopK(self, word_list, k):
        score_list = []
        # print ["Hello Here", word_list, self.sort_dic['company']]

        # note all id s of the word list
        id_word_list = []
        for item in word_list:
            if item in self.sort_dic:
                id_word_list.append(self.sort_dic[item])

        print ["Hello World", id_word_list]

        for i in range(0, self.dos_len):
            score_list.append(self.cosineScore(id_word_list, i))

        # print score_list
        # file_id = sorted(file_id.iteritems(), key=lambda asd: asd[0])

        file_id = [-1 for x in range(0, k)]
        score_id = [-1 for x in range(0, k)]
        count = 0
        for score in score_list:
            temp_score = min(score_id)
            if score > temp_score:
                index = score_id.index(temp_score)
                file_id[index] = count
                score_id[index] = score
            count = count + 1
        # print score_id
        count = 0
        for score in score_id:
			if score <= 0:
				file_id[count] = -1
			count = count + 1;
        return file_id




