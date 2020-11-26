# for every new user we would need a profile to be created automatically
# before this file was created it was being done by the admin section

# we're gonna import a signal
from django.db.models.signals import post_save
# this is a signal when gets fired after an object is saved
# in this case we want a get a post_save signal when a user is created
# so we would also need the built in user model

from django.contrib.auth.models import User #its going to be a sender of the signal
# we also need reciever which will be a function that gets this signal and performs some tasks

from django.dispatch import receiver #reciever 

# we also need the profile import since we need to create a profile inside our function
from .models import Profile

@receiver(post_save, sender=User) #reciever is a decorator
def create_profile(sender,instance,created,**kwargs):
    if created:
        print('Signal Fired')
        Profile.objects.create(user=instance)

#we need to save this profile as well
@receiver(post_save, sender=User) #reciever is a decorator
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

# we still need to import this signal in our user/apps.py, inside ready function