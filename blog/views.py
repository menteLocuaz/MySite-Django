from django.shortcuts import render
from .models import Post
from django.http import Http404


def pos_list(request):
    posts = Post.publish.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request):
    try:
        post = Post.publish.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post Found")

    return render(request, "blog/post/detail.html", {"post": post})
