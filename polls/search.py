# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from logics.Search import search_inv_final


# 表单
class Res:

    docFile = ""
    text = ""

    def __init__(self, file_name, text):
        self.docFile = file_name
        self.text = text


def search_form(request):
    return render_to_response('single_search.html')


def advanced_search_form(request):
    return render_to_response('advanced_search.html')


# 接收请求数据
def search1(request):

    request.encoding = 'utf-8'

    if 'and' in request.GET:
        s1 = request.GET['and'].encode('utf-8')
    if 'q' in request.GET:
        s1 = request.GET['q'].encode('utf-8')
    if 'q' in request.GET:
        s1 = request.GET['q'].encode('utf-8')
    if 'q' in request.GET:
        s1 = request.GET['q'].encode('utf-8')
        res_list = search_inv_final(request.GET['q'].encode('utf-8'), [], [], [])
        print res_list
        message = "docID: "
        for doc_id in res_list:
            message += str(doc_id) + " "
        if len(res_list) == 0:
            message += "nothing found"
    else:
        message = '你提交了空表单'

    return HttpResponse(message)


def show_details(request):
    return render_to_response('15920.html')


def search(request):

    total = 0
    t = 0
    s = 0
    res = ['15920.html', '15920.html', '15920.html']

    if 'q' in request.GET and request.GET['q']:
        return render_to_response('result.html',
                                  {'total_found': total, 'use_time': t, 'summary': s, 'matches': res})
    else:
        return render_to_response('single_search.html', {'error': True})


def adv_search(request):

    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""

    if 'and' in request.GET and request.GET['and']:
        s1 = request.GET['and'].encode('utf-8')
    if 'comp' in request.GET and request.GET['comp']:
        s2 = request.GET['comp'].encode('utf-8')
    if 'or' in request.GET and request.GET['or']:
        s3 = request.GET['or'].encode('utf-8')
    if 'not' in request.GET and request.GET['not']:
        s4 = request.GET['not'].encode('utf-8')

    if s1 != "" or s2 != "" or s3 != "" or s4 != "":
        res_tuple = search_inv_final(s1, s2, s3, s4)
        res_list = []
        for rest in res_tuple[1]:
            res = Res(rest[0], rest[1])
            res_list += [res]

        return render_to_response('result.html', {'tag': res_tuple[0], 'res_list': res_list})

    # res_tuple = (tag, [(filename1, text1), (filename2, text2), ...])
    # tag == 1: 矫正后高
    else:
        return render_to_response('advanced_search.html', {'error': True})
