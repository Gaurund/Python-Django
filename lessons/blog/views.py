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

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birth_date = form.cleaned_data['birth_date']
            author = Author(
                first_name=first_name,
                last_name=last_name,
                email=email,
                bio=bio,
                birth_date=birth_date,
            )
            author.save()
            logger.info(f'{first_name} {last_name} внесён в базу')

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
