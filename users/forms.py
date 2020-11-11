from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #required is set to True

    # This meta will give us a nested namespace for configurations
    # also keeps the configurations in one place
    # within the configuration we're saying that the model that will be affected is the user model
    # if we do form.save() its going to save it to this user model 
    #fields list shows the form sections and in what order we want them 
    # now go to views.py of this app and inherit over there
    class Meta:
        model = User
        fields = ['username','email','password1','password2']   
