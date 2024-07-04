from django.shortcuts import render

# Create your views here.
 
from .models import Post
def home(request):
    posts = Post.objects.all()
    return render(request, 'main.html',{'posts':posts})


def post(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html',{'post':post})