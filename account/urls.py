from django.urls import path, include
from django.views.generic import TemplateView
from todoapp.views import TodoList, TodoDetail

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('list', TodoList.as_view(template_name='EventList.html'), name='EventList'),
    path('event/<int:pk>', TodoDetail.as_view(template_name='EventDetail.html'), name='EventDetail')

        ]