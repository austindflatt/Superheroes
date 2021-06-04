from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SuperHeroes
from django.urls import reverse

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


def create(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('superhero_name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('secondary_ability')
        new_superhero = SuperHeroes(superhero_name=superhero_name, alter_ego_name=alter_ego_name, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('Superhero:index'))
    else:
        return render(request, 'Superhero/create.html')


def edit(request, superhero_id):
    hero = SuperHeroes.objects.get(id=superhero_id)
    if request.method == 'POST':
        hero.superhero_name = request.POST.get('superhero_name')
        hero.alter_ego_name = request.POST.get('alter_ego_name')
        hero.primary_ability = request.POST.get('primary_ability')
        hero.secondary_ability = request.POST.get('secondary_ability')
        hero.catchphrase = request.POST.get('secondary_ability')
        hero.save()
        return HttpResponseRedirect(reverse('Superhero:index'))
    else:
        context = {
            'hero': hero
        }
        return render(request, 'Superhero/edit.html', context)


def delete(request, superhero_id):
    hero = SuperHeroes.objects.get(id=superhero_id)
    hero.delete()
    all_superheroes = SuperHeroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'Superhero/index.html', context)
