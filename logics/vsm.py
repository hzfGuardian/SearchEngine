
from query import *
import math
import numpy as np
# import scipy as sp


class VSM:

    matrix = np.zeros
    dic = {}
    sort_dic = {}   # record the sort id for each item

    def __init__(self, docs, dicts):
        self.dic = dicts
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

    def cosineScore(self, query, doc_id):
        vq = self.qryVector(query)
        vd = self.matrix[:, doc_id]
        if np.linalg.norm(vq) == 0 or np.linalg.norm(vd, 2) == 0:
            return 0
        else:
            return np.inner(vq, vd) / (np.linalg.norm(vq) * np.linalg.norm(vd, 2))


    def getTopK(self, k):
        return




