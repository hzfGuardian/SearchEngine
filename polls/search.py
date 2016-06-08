# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from logics.buffer import f


# 表单
def search_form(request):
    return render_to_response('single_search.html')


# 接收请求数据
def search(request):

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
