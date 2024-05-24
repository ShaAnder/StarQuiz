from django.shortcuts import render, get_object_or_404
from .models import Planet

def index(request):
    return render(request, 'frontend/index.html')

def galaxy_map(request):
    planets = Planet.objects.all()
    return render(request, 'frontend/galaxy.html', {'planets': planets})

def planet_detail(request, planet_id):
    planet = get_object_or_404(Planet, pk=planet_id)
    characters = planet.characters.all()
    trivia = planet.trivia.all()
    return render(request, 'frontend/planet_detail.html', {'planet': planet, 'characters': characters, 'trivia': trivia})