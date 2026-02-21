from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'blog/home.html', {
        'blogs': blogs,
        'comment_form': comment_form
    })


@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.user != blog.author and not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/edit_blog.html', {'form': form})


@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.user == blog.author or request.user.is_superuser:
        blog.delete()

    return redirect('home')


@login_required
def add_comment(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()

    return redirect('home')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')