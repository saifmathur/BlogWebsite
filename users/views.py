from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm 
#since we're no longer using the default UserCreationForm since we created our own
# commenting that import 
from django.contrib import messages

# the log in required decorator
from django.contrib.auth.decorators import login_required


#importing the changed form from forms.py which we created
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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


'''in order to prevent anyone from going back to the profile page after logging out,
    this can be done by typing '/profile' in the URL, to prevent this we need a 
    log in required decorator provided by django '''

@login_required  #this is a decorator
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #this 'instance = request.user' parameter populates the update form with the current
        #information of the user 
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES , #the images coming in
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            # then we save the data
            u_form.save()
            p_form.save()
            print(request.user,' PROFILE UPDATED')
            messages.success(request, f'Account has been updated.')
            #gonna redirect the user to the profile page
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        #this 'instance = request.user' parameter populates the update form with the current
        #information of the user 
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html',context)
