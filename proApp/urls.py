from django.conf.urls import url
from django.urls import path,re_path,include
from django.views.static import serve
from proweb import settings
from . import views
from django.conf.urls.static import static

import os
urlpatterns = [
	url(r'^search$',views.user,name='search'),
	url(r'^$',views.index,name='index'),
	re_path(r'upfile/(?P<path>.*)$',serve,{'document_root':settings.MDEIA_ROOT}),
]

	