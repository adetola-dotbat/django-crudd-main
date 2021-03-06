from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy("blog:all")

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy("blog:all")
