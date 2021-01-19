from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    #things you want to save
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    #after this, you're supposed to run the makemigrations command
    #that will create an initial file under the app/migrations directory
    #AFTER EVERY MODEL CREATION YOU HAVE TO RUN THE makemigrations COMMAND
    # run this after 'py manage.py sqlmigrate blog 0001'
    #this will show the sql command it will run in order to create your model
    #after this run the migrate command
    #you can also use the django python shell to interact with these models
    #use py manage.py shell
    #import the model that you've created, in this case its 'Post' along with the User model
    #import this Post model will be 'from blog.models import Post'
    #at this point we already have two users so we cant fetch all users by the command 'Users.objects.all()', this is for python shell
    ''' 
        SHELL COMMANDS
        1. User.objects.first()
        2. User.objects.filter(username='saif')
        3. Users.objects.all()
        4. User.objects.filter(username='saif').first()
        5. user = User.objects.filter(username='saif').first()
            5.1. user.id, user.pk
    '''
    '''
    You can do the same with Posts and just use the command Post.objects.all() which will 
    give an empty array since we dont have any Posts in there

    eg to create a post
    post_1 = Post(titel='Blog 1', content='First post content!', author = user)
    after doing this you still need to save this post var by using post_1.save()
    now since the post is created you can access the post by creating an object 

    post = Post.objects.first()
    post.title
    post.date_posted

    user.post_set.all() gives all the post
    you can also create posts using this

    user.post_set.create(title='blog 3', content='third post content!') now the author of this post
    will be the username that was assigned to the 'user' object

    now this will be useful in the file views.py where initially it was static data
    but now importing the models will make it dynamic and cleaner

    the post will have a property in which we have to tell django that when we access this post
    what will we get by default, in this case we want the post title
    so under Post class we create a method __str__(self)
    '''
    