

from .models import Todo, Category, User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404


class TodoList(LoginRequiredMixin,ListView):

    paginate_by = 5

    allow_empty = True
    context_object_name = 'event_list'

    def get_queryset(self):
        user = self.request.user
        return user.events.filter(author=user)

class TodoDetail(LoginRequiredMixin,DetailView):
    model = Todo

#TODO: Prepare The template,To Show The Events.
#TODO: config the webapp for errors like 4xx,5xx
