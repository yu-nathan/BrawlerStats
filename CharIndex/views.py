from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Character, Stats

# Create your views here.
class CharacterDetails(generic.DetailView):
    model = Stats
    template_name = 'charIndex/detail.html'
    context_object_name = 'character'

    def get_object(self):
        return get_object_or_404(Character, char_name=self.kwargs['char_name'],
            char_origin=self.kwargs['char_origin'])
