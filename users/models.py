from django.db import models

'''
By default, the django users model doesn't give the user the ability 
to upload profile pictures, so we need to modify that by creating our own class and extending the default class
1. Extend the user model
2. create a new profile model, that has a one-to-one relationship with the user
    i.e A profile can have only one picture, a picture can belong to only one profile
'''
# Create your models here.
from django.contrib.auth.models import User
from PIL import Image #for profile resizing

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #CASCADE, if the user is deleted then delete the profile
    #we want a one to one relationship with the user model
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    #NOTE: you need pillow lib for storing images
    '''
    Now, we create a dunder str method so that when we print this out
    it will display how we want it to be displayed
    basically if we dont have this its just gonna print out the profile object 
    and we want it to be more descriptive
    '''
    def __str__(self): #self is the instance
        return f'{self.user.username} Profile'

    # since we have created a model we need those migrations
    # so run py manage.py makemigrations
    # and then py manage.py migrate
    # Since we need to view these profiles in the admin side we need to register this
    # model with the admin side
    
    def save(self, *args, **kwargs):
        #this method already exists we're just over writing it
        super().save() #we're gonna run the save method of the parent class by super()
        #now we're gonna resize the profile picture
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) 