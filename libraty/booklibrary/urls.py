from django.conf.urls import url
from . import views
app_name = 'booklibrary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^readerlogin/$', views.readerlogin, name='readerlogin'),
    url(r'^reader/$', views.reader, name='reader'),
    url(r'^readerregister/$', views.readerregister, name='readerregister'),
    url(r'^readerlogout/$', views.readerlogout, name='readerlogout'),
    url(r'^readerquery/$', views.readerquery, name='readerquery'),
    url(r'^reader/book/(\d+)/$', views.book, name='book'),
    url(r'^reader/info/$', views.readerinfo, name='readerinfo'),
    url(r'^reader/modify/$', views.readermodify, name='readermodify'),
    url(r'^reader/history/$', views.readerhistory, name='readerhistory'),

    url(r'^echarts/$', views.echarts, name='echarts')

]