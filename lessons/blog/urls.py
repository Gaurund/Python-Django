from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_blog, name='index_blog'),
    path('about/', views.about_blog, name='about_blog'),
    path('author/<int:author_pk>/posts/', views.author_posts, name='author_posts'),
    path('author/<int:author_pk>/', views.author_pk, name='author_pk'),
    path('post/<int:post_pk>', views.post, name='post'),
    path('author/add/', views.add_author, name='add_author'),
    path('post/add/', views.add_post, name='add_post'),
]