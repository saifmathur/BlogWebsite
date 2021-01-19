from django.urls import path
from . import views
from . views import PostListView


urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

# when we use class based views we need to convert the class into an actual view by using the 'as_view()' method
# now this change will give an error
# what it was looking for was <app>/<model>_<viewtype>.html

