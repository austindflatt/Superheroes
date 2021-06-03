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


def detail(request, superhero_id):
    hero = SuperHeroes.objects.get(id=superhero_id)
    context = {
        'hero': hero
    }
    return render(request, 'Superhero/details.html', context)
