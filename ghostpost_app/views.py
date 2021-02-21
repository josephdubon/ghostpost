from django.shortcuts import render, redirect
from ghostpost_app.models import Post


def index_view(request):
    name = 'Ghost Post'
    posts = Post.objects.all()
    return render(request, 'home.html', {'app_name': name, 'posts': posts})


def like_view(request, post_id):
    # filter id will bring a query -> using .first gives access to first item
    post = Post.objects.filter(id=post_id).first()
    post.likes += 1
    # must run .save() to save to database
    post.save()
    return redirect('/')


def dislike_view(request, post_id):
    pass
