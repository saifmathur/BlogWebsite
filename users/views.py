from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm 
#since we're no longer using the default UserCreationForm since we created our own
# commenting that import 
from django.contrib import messages

#importing the changed form from forms.py which we created
from .forms import UserRegisterForm


'''
after this, installed crispy forms and go to installed apps in the project folder
and add this 'crispy_forms' in the list

also you have to tell crispy_forms which css framework you want to use
the default is bootstrap2 and we need 4
so add this line to the bottom of the page
CRISPY_TEMPLATE_PACK = 'bootstrap4'

'''



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
            messages.success(request, f'Account created for {username}! You can now Login.')
            #gonna redirect the user to the log in page
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


