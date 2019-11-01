# Views for the app homeSite
from django.views import generic
from django.utils import timezone

from charIndex.models import Character


# Create your views here.
class IndexView(generic.ListView):
    model = Character
    template_name = 'CharacterNexus/index.html'
    context_object_name = 'newest_characters_list'

    def get_queryset(self):
        return Character.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
