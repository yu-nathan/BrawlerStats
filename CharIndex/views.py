# Views for the app charIndex.
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q

from .models import Character, Stats

# Create your views here.
class CharacterDetailsView(generic.DetailView):
    model = Stats
    template_name = 'charIndex/detail.html'
    context_object_name = 'character'

    def get_object(self):
        return get_object_or_404(Character, char_name=self.kwargs['char_name'],
            char_origin=self.kwargs['char_origin'])

class SearchResultsView(generic.ListView):
    model = Character
    template_name = 'CharacterNexus/search_results.html'
    context_object_name = 'relevant_characters'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Character.objects.filter(
            Q(char_name__icontains=query) | Q(char_origin__icontains=query)
        )
