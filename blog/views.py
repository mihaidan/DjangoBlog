from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import PostForm


# List view of posts.
def post_list(request):
    # pulling all posts from database as an object list
    post_list = Post.objects.all()

    context = { 'post_list': post_list }

    # using post_list template, render the information
    return render(request, 'blog/post_list.html', context)

# Detailed view of the posts.
def post_description(request, slug):
    # pull specific post based on the slug, or return a 404 not found
    post_object = get_object_or_404(Post, slug=slug)

    context = {'post': post_object }

    # using post_desc template, render the information
    return render(request, 'blog/post_desc.html', context)

# Creating a post.
def create_post(request):
    # pull the information from the request
    new_post = PostForm(request.POST or None)

    # adding a try and except for messages to be displayed
    try:
        # check if post is valid, then save
        if new_post.is_valid():
            new_post.save()
            messages.success(request, "Post succesfully saved!")
    except Exception as e:
        messages.warning(request, "Post failed to save: {}.".format(e))

    context = { 'post': new_post }

    return render(request, 'blog/create_post.html', context)

# Editing a post.
def edit_post(request, pk):
    # pull the edit post from the Post table based on the primary key.
    e_post = get_object_or_404(Post, pk=pk)

    # adding a try and except for messages to be displayed
    try:
        # check if the request is a POST
        if request.method == 'POST':
            # update the post, and if it's valid, save it to the database
            edit = PostForm(request.POST, instance=e_post)

            if edit.is_valid():
                edit.save()
                messages.success(request, "Post succesfully edited!")
        # if it's not, leave the post alone
        else:
            edit = PostForm(instance=e_post)
    except Exception as e:
        messages.warning(request, "Post failed to save: {}.".format(e))

    context = { 'post': edit }

    return render(request, 'blog/create_post.html', context)