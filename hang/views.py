from django.shortcuts import render
from django.http import HttpResponse
from .game import Game

def index(request):
    g = Game()
    g.play(4,"word")
    
    context = {"title" : "Hangman", "screen" : str.join("\n", g.output)}
    return render(request, 'hang/index.html', context)
    
def other(request):
    context = {"name" : "Bruno"}
    return render(request, 'hang/other.html', context)

