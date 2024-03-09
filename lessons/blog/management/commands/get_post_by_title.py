from django.core.management.base import BaseCommand
from blog.models import Author, Post

class Command(BaseCommand):
    help = "Get posts by title."

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title of the post')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        post = Post.objects.filter(title__contains=title).first()
        self.stdout.write(f'{post}')
