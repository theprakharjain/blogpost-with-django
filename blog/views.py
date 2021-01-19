from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})

