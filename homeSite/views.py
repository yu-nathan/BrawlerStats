from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.DetailView):
    template_name = 'CharacterNexus/index.html'
