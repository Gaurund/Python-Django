from django.core.management.base import BaseCommand
from blog.models import Author, Post


class Command(BaseCommand):
    help = "Create a post."

    def add_arguments(self, parser):
        parser.add_argument('author_pk', type=int, help='ID of the author')
        parser.add_argument('title', type=str, help='Title for the post')
        parser.add_argument('content', type=str, help='Content of the post')
        parser.add_argument('is_published', type=bool, help='Is it published?')

    def handle(self, *args, **kwargs):
        author_pk = kwargs.get('author_pk')
        author = Author.objects.filter(id__exact=author_pk).first()
        if author is None:
            return f'An author with id {author_pk} is not exists. The input was rejected.'
        title = kwargs.get('title')
        content = kwargs.get('content')
        is_published = kwargs.get('is_published')
        post = Post(
            title=title,
            content=content,
            author_id=author_pk,
            is_published=is_published
        )
        post.save()
        self.stdout.write(f'{post}')
