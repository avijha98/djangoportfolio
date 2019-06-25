
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^posts/$',views.post_list, name ='post_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'),
    url(r'^posts/(?P<pk>[0-9]+)/post_comment/$',views.post_comment,name='post_comment'),
    url(r'^posts/(?P<pk>[0-9]+)/post_comment/add_comment/$',views.add_comment,name='add_comment'),
]
