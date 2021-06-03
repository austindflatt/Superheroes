from django.shortcuts import render
from django.http import HttpResponse
from .models import SuperHeroes

# Create your views here.


def index(request):
    all_superheroes = SuperHeroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'Superhero/index.html', context)