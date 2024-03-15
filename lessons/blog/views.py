import logging

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import *
from .models import Post, Author

logger = logging.getLogger(__name__)


def index_blog(request):
    logger.info('Blog page accessed')
    return HttpResponse("It is a blog page")


def about_blog(request):
    pass


def author_posts(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    posts = Post.objects.filter(author=author)
    context = {
        'title': "Все посты",
        'author': author,
        'posts': posts
    }
    template_name = 'blog/posts.html'
    return render(request, template_name, context)


def post(request, post_pk):
    post_ = get_object_or_404(Post, pk=post_pk)
    post_.views += 1
    post_.save()
    context = {
        'post': post_
    }
    template_name = 'blog/post.html'
    return render(request, template_name, context)


def author_pk(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    template_name = 'blog/author.html'
    context = {
        'title': f'Автор: {author.full_name}',
        'author': author,
    }
    return render(request, template_name, context)


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            cleaned_data = form.cleaned_data
            author = Author(**cleaned_data)
            author.save()
            logger.info(f'Автор внесён в базу')

    else:
        form = AuthorForm()
        message = 'Введите данные автора'

    context = {
        'title': 'Автор',
        'form': form,
        'message': message,
    }
    template_name = 'blog/add_author.html'

    return render(
        request,
        template_name,
        context
    )


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_ = Post(**cleaned_data)
            post_.save()
            logger.info(f'Пост внесён в базу')

    else:
        form = PostForm()
        message = 'Введите пост'

    context = {
        'title': 'Пост',
        'form': form,
        'message': message,
    }
    template_name = 'blog/add_post.html'

    return render(
        request,
        template_name,
        context
    )
