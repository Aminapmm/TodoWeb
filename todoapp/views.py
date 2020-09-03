from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.shortcuts import render, redirect
from .models import Todo, Category, User
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class TodoList(LoginRequiredMixin,ListView):

    allow_empty = True
    context_object_name = 'event_list'

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)


# Create your views here.
@require_GET
def index(request):
    return render(request, 'index_2.html')


def todolist(request, slug):
    return render(request, 'base.html', context={'todo_list': Todo.objects.filter(slug=slug)})


#TODO:ADD LAST DATETIME,THAT THE AUTHOR EDITED THE TODO,NOTE...