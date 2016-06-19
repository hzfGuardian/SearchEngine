"""SearchEngine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views import static
import polls.search
import settings

urlpatterns = [
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_PATH}),
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', polls.search.search1),
    url(r'^search-form/$', polls.search.search_form),
    url(r'^Reuters/(.+).html$', polls.search.show_details),
    url(r'^asearch/$', polls.search.advanced_search_form),
    url(r'^advanced-search/$', polls.search.adv_search)
]
