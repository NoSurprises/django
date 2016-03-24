from django.shortcuts import render, get_object_or_404
from .models import Post 
# hello from github
    
from django.shortcuts import redirect
# Create your views here.

def home(request):
    posts = Post.objects.filter(draft=False)
    context = {
        'posts': posts,
    
    }
    return render(request, 'blog/home.html', context)
    


def redirect_to_blog(request):
    return redirect('/blog')
    
    
def detail(request, slug=None):

    post = get_object_or_404(Post, slug=slug)
    
    
    context = {
        'post': post,
    
    }
    
    
    return render(request, 'blog/detail.html', context)
