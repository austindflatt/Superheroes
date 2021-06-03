from django.shortcuts import render
from django.http import HttpResponse
from .models import SuperHeroes

# Create your views here.


def index(request):
    all_superheros = SuperHeroes.objects.all()
    return render(request, 'Superhero/index.html')