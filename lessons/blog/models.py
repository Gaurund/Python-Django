from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birth_date = models.DateField(default=timezone.now)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Author: {self.full_name}, email: {self.email}, birth day: {self.birth_date}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'Title is "{self.title}". And text is "{self.content}".'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:5])}...'

