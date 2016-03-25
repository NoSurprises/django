from django.shortcuts import render, get_object_or_404

from .models import Post, Comment
from .forms import AddCommentForm
from django.http import HttpResponseRedirect

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
    
    if request.POST:
        form = AddCommentForm(request.POST)
        new_comment = form.save(commit=False)
        new_comment.post = get_object_or_404(Post, slug=slug)
        if form.is_valid():
            new_comment.save()
            return HttpResponseRedirect('/blog/' + slug)
            
        
            
        
        
    else:
        form = AddCommentForm()
        
    
    
    post = get_object_or_404(Post, slug=slug)
    
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        
    }
    
    
    return render(request, 'blog/detail.html', context)
    

    
def plus(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    post.rating += 1
    post.save()
    return HttpResponseRedirect('/blog/' + slug)
    
    
    
def minus(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    post.rating -= 1
    post.save()
    return HttpResponseRedirect('/blog/' + slug)
    
    
    
    
    
