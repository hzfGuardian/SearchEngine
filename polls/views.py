from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response


# 搜索框主页
def search_form(request):
    return render_to_response('single_search.html')


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

