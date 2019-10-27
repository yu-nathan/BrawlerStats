# Views for the app homeSite
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
