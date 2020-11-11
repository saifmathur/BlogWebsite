from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm 
#since we're no longer using the default UserCreationForm since we created our own
# commenting that import 
from django.contrib import messages

#importing the changed form from forms.py which we created
from .forms import UserRegisterForm

# types of messages
# messages.info
# messages.success
# messages.warning
# messages.error

# Create your views here.

#gonna use predefined forms
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('FORM VALID')
            form.save() #saving the user
            username = form.cleaned_data.get('username') #its a dictionary
            messages.success(request, f'Account created for {username}!')
            #gonna redirect the user back to the home page
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


