from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Posts
def get_all(request):
    """
    Create a view that will return a list
    of Bugs and Feature Requests sorted in descending order depending on number 
    of upvotes that were published prior to 'now' and render them to the 
    'blogposts.html' template
    """
    post_list = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-upvotes')
    paginator = Paginator(post_list, 10) # Show 10 posts per page
    
    page = request.GET.get('page')
    posts = paginator.page(1)
    return render(request, "all.html", {'posts': posts})
    
def get_features(request):
    """
    Create a view that will return a list
    of Feature Requests sorted in descending order depending on number of 
    upvotes that were published prior to 'now' and render them to the 
    'features.html' template
    """
    post_list = Post.objects.filter(type="Feature Request", published_date__lte=timezone.now()
        ).order_by('-upvotes')
    paginator = Paginator(post_list, 10) # Show 10 posts per page
    
    page = request.GET.get('page')
    posts = paginator.page(1)
    return render(request, "features.html", {'posts': posts})
    
def get_bugs(request):
    """
    Create a view that will return a list
    of Bugs sorted in descending order depending on number of upvotes that were 
    published prior to 'now' and render them to the 'features.html' template
    """
    post_list = Post.objects.filter(type="Bug", published_date__lte=timezone.now()
        ).order_by('-upvotes')
    paginator = Paginator(post_list, 10) # Show 10 posts per page
    
    page = request.GET.get('page')
    posts = paginator.page(1)
    return render(request, "bugs.html", {'posts': posts})

def post_detail(request, pk):
    """
    Create a view that returns a single Feature or Bug Post object based on the 
    post ID (pk) and render it to the 'postdetail.html' template. Or return a 
    404 error if the post is not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})
    
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows users to create or edit posts depending on if the 
    Post ID is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(post_detail, instance.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'postform.html', {'form': form})
    
def delete_post(request, pk):
    """
    Create a view that allows users to delete posts.
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return redirect(reverse('get_all'))