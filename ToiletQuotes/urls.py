from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
 
    url(r'^home/', views.home, name='home'),
    url(r'^addQuote/', views.addQuote, name='addQuote'),
    url(r'^getQuotes/', views.getQuotes, name='getQuotes'), # for android
    url(r'^showQuotes/', views.showQuotes, name='showQuotes'),
    url(r'^statistics/', views.stats, name='stats'),
    url(r'^insertQuote/', views.insertQuote, name='insert'),
    url(r'^delete/(?P<quote_id>[0-9]+)/(?P<act_pass>\w{0,50})/', views.delete, name='del'),
    url(r'^confirm/(?P<quote_id>[0-9]+)/(?P<act_pass>\w{0,50})/', views.confirm, name='confirm'),
)
