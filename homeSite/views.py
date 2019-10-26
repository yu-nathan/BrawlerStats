# Views for the app homeSite
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse

from charIndex.models import Character, Stats

# Create your views here.
def index(request):
    template_name = 'CharacterNexus/index.html'
    newest_characters_list = Character.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {'newest_characters_list': newest_characters_list}
    return render(request, template_name, context)
