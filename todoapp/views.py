from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpRequest, HttpResponse
from .models import Todo, Category, User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
class TodoList(LoginRequiredMixin,ListView):

    paginate_by = 5

    allow_empty = True
    context_object_name = 'event_list'

    def get_queryset(self):
        user = self.request.user
        return user.events.filter(author=user)



#TODO: Prepare The template,To Show The Events.
#TODO: config the webapp for errors like 4xx,5xx
