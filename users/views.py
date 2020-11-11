from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# types of messages
# messages.info
# messages.success
# messages.warning
# messages.error

# Create your views here.

#gonna use predefined forms
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') #its a dictionary
            messages.success(request, f'Account created for {username}!')
            #gonna redirect the user back to the home page
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


