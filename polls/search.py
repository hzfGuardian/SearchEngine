# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from logics.Search import search_inv_final, search_vsm
import time


# 表单
class Res:

    docFile = ""
    text = ""

    def __init__(self, file_name, text):
        self.docFile = file_name
        self.text = text


def search_form(request):
    s_time = time.time()
    if 'vsm' in request.GET and request.GET['vsm']:
        s = request.GET['vsm'].encode('utf-8')
        res_tuple = search_vsm(s)
        res_list = []

        for rest in res_tuple[1]:
            res = Res(rest[0], rest[1])
            res_list += [res]
            print res.text

        num = len(res_list)
        e_time = time.time()
        # print
        return render_to_response('result.html', {'tag': res_tuple[0], 'res_list': res_list, 'num': num, 'time': e_time - s_time})
    else:
        return render_to_response('result.html', {'error': True})


def advanced_search_form(request):
    return render_to_response('advanced_search.html')


def show_details(request, param):
    return render_to_response('Reuters/' + param + '.html')


def search(request):
    return render_to_response('single_search.html')


def adv_search(request):

    s_time = time.time()
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""

    similar_tag = 0  # use similar search

    if 'and' in request.GET and request.GET['and']:
        s1 = request.GET['and'].encode('utf-8')
    if 'comp' in request.GET and request.GET['comp']:
        s2 = request.GET['comp'].encode('utf-8')
    if 'or' in request.GET and request.GET['or']:
        s3 = request.GET['or'].encode('utf-8')
    if 'not' in request.GET and request.GET['not']:
        s4 = request.GET['not'].encode('utf-8')
    if 'check' in request.GET and request.GET['check']:
        similar_tag = request.GET['check'].encode('utf-8')
    if 'search' in request.GET and request.GET['search']:
        s1 = request.GET['search'].encode('utf-8')

    if s1 != "" or s2 != "" or s3 != "" or s4 != "":
        res_tuple = search_inv_final(similar_tag, s1, s2, s3, s4)
        res_list = []

        for rest in res_tuple[1]:
            res = Res(rest[0], rest[1])
            res_list += [res]
            print res.text

        num = len(res_list)
        # print
        e_time = time.time()
        # print e_time - s_time
        return render_to_response('result.html', {'tag': res_tuple[0], 'res_list': res_list, 'num': num, 'time': e_time - s_time})

    # res_tuple = (tag, [(filename1, text1), (filename2, text2), ...])
    # tag == 1: 矫正后高
    else:
        return render_to_response('advanced_search.html', {'error': True})
