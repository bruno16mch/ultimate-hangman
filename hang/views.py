from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {"title" : "Hangman"}
    return render(request, 'hang/index.html', context)
    
def other(request):
    context = {"name" : "Bruno"}
    return render(request, 'hang/other.html', context)
# Create your views here.
