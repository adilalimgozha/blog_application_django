from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm

# Create your views here.
from django.http import HttpResponse
from .models import Post, Comment

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})


def post_list(request):
    my_posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': my_posts})

def post_detail(request, post_id):
    mypost = get_object_or_404(Post, id=post_id)

    mycomments = Comment.objects.filter(post=mypost)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = mypost 
            if request.user.is_authenticated:
                comment.author = request.user
            else:
                comment.author = None
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()  

    return render(request, 'post_detail.html', {'post': mypost, 'form': form, 'comments': mycomments})

def edit_post(request, post_id):
    mypost = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=mypost)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=mypost.id) 
    else:
        form = PostForm(instance=mypost)

    return render(request, 'post_form.html', {'form': form, 'post': mypost})

def delete_post(request, post_id):
    mypost = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        mypost.delete()
        return redirect('post_list')

