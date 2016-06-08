# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from logics.buffer import f


# 表单
def search_form(request):
    return render_to_response('single_search.html')


# 接收请求数据
def search1(request):

    request.encoding = 'utf-8'

    if 'q' in request.GET:
        res_list = f(request.GET['q'].encode('utf-8'))
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
