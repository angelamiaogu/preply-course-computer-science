from .views import home, post
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('post/<slug:slug>', post, name='post'),
]


