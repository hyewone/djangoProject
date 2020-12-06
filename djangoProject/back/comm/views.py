from django.http import HttpResponse
from django.shortcuts import  render

def index(request):
    return HttpResponse('Hi There')

def indexHtml(request):
    msg = 'Show Me The Django'
    return render(request, 'index.html', { 'msg' : msg })