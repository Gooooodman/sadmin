from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('YunWei.views',

#yunwei
    url(r'^listqq/$', 'yunwei.ListQQ', name='listqq'),
    url(r'^listyy/$', 'yunwei.ListYY', name='listyy'),
    url(r'^listtw/$', 'yunwei.ListTW', name='listtw'),
    #url(r'^listtw/$', 'yunwei.ListTW', name='listtw'),
    url(r'^cdn/$', 'yunwei.UpdateCDN', name='updatecdn'),
)
