from django.utils import timezone
from django.shortcuts import render, redirect
from ghostpost_app.models import Post
from ghostpost_app.forms import CreatePostForm


def index_view(request):
    name = 'Ghost Post'
    posts = Post.objects.all()
    return render(request, 'home.html', {'app_name': name, 'posts': posts})


def boast_view(request, post_id):
    # get post
    post = Post.objects.filter(id=post_id).first()
    # add like
    post.boasts += 1
    # must run .save() to save to database
    post.save()
    # redirect home for good ux
    return redirect('/')


def roast_view(request, post_id):
    # get post
    post = Post.objects.filter(id=post_id).first()
    # add dislike
    post.roast += 1
    # must run .save() to save to database
    post.save()
    # redirect home for good ux
    return redirect('/')


def create_post(request):
    context = {}

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                text=data['text'],
                boast=data['boasts'],
                roast=data['roast'],
                created_at=timezone.now,
            )
            return redirect('/')

    form = CreatePostForm()
    context.update({'form': form})
    return render(
        request,
        'generic_form.html',
        context
    )
