from django.shortcuts import render, redirect
from .models import *
from apps.contact.models import Subscribe
from .forms import CommentForm


# Create your views here.

def blog(request):
    posts = Post.objects.order_by('-id')
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('.')
    ctx = {
        'posts': posts
    }
    return render(request, 'blog.html', ctx)


def blog_single(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    next_issue = Post.objects.filter(id__gt=post.id).first()
    prev_issue = Post.objects.filter(id__lt=post.id).first()
    if form.is_valid():
        com = form.save(commit=False)
        com.post = post
        com.save()
    ema = request.GET.get('email')
    if ema:
        Subscribe.objects.create(email=ema)
        return redirect('.')
    ctx = {
        'post': post,
        'form': form,
        'next_issue': next_issue,
        'prev_issue': prev_issue,
    }
    return render(request, 'blog-details.html', ctx)
