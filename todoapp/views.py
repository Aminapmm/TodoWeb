from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods , require_GET
from django.shortcuts import render

# Create your views here.
@require_GET
def index(request):
    return render(request, 'index_2.html')
