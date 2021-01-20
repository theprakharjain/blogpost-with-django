from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Overriding the form_valid method and providing the author id of current logged in author
    def form_valid(self, form):
        form.instance.author = self.request.user
        # Running form valid method on the parent class
        return super().form_valid(form)

# Mixins should always be on the left or we can say before the UpdateView parameter
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Overriding the form_valid method and providing the author id of current logged in author
    def form_valid(self, form):
        form.instance.author = self.request.user
        # Running form valid method on the parent class
        return super().form_valid(form)

    # function need to write under "UserPassesTestMixin" to get the same user check
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # creating success url
    success_url = '/'

    # function need to write under "UserPassesTestMixin" to get the same user check
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})

