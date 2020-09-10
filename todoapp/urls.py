from django.contrib.auth import login
from django.urls import path, re_path
from .views import *


urlpatterns = [

    #path('', TodoList.as_view(template_name='list.html'), name='index'),
    path('<slug:slug>', TodoList.as_view, name='todolist'),
    re_path('^login/.*$', login, name='login'),

]
