from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_blog, name='index_blog'),
    path('about/', views.about_blog, name='about_blog'),
    path('author/<int:author_pk>/posts/', views.author_posts, name='author_posts'),
    path('post/<int:post_pk>', views.post, name='post')
]