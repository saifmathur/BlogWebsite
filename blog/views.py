from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
posts = [
    {
        'author':'Saif Mathur',
        'title':'Blog Post 1',
        'content':'some content for the first blog',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'some content for the second blog',
        'date_posted': 'August 28, 2018'
    },
    {
        'author':'Prison Mike',
        'title':'Blog Post 3',
        'content':'some content for the third blog',
        'date_posted': 'March 10, 2018'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts':posts,
        'title' : 'Home',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})