from django.shortcuts import render
from .models import Post, Comment
from market.user.models import User
from django.db.models import Count, F
from .forms import CommentForm


def blog_list(request):
    posts = Post.objects.annotate(
        comment_count=Count("comment"),
        author_name=F("author__username")
    ).values('id', 'title', 'image', 'content', 'post_date', 'comment_count', 'author_name')

    print(posts)

    context = {
        "posts": posts
    }
    return render(request, 'blog.html', context)


def blog_detail(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        print(form, form.is_valid())
        if form.is_valid():
            comment = form.save()
            comment.post = Post.objects.get(id=pk)
            comment.author = request.user
            comment.save()
            print(comment)

    post = Post.objects.annotate(
        comment_count=Count("comment"),
        author_name=F("author__username")
    ).filter(pk=pk).values('id', 'title', 'image', 'content', 'post_date', 'comment_count', 'author_name')
    comments = Comment.objects.filter(post_id=pk).select_related('author').order_by('-comment_date')
    form = CommentForm()
    context = {
        "post": post[0],
        "comments": comments,
        "form": form
    }
    return render(request, 'blog_detail.html', context)
