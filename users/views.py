from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#gonna use predefined forms
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

    