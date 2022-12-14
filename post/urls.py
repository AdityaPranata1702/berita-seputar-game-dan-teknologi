from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('posts/', posts, name='posts'),
    path('users/', users, name='users'),
    path('profile/', profile, name='profile'),
    path('content/', content, name='content'),
    path('sinkron/', sinkron, name='sinkron'),
    path('posts/plus/', plus, name='plus'),
    path('posts/visited/<int:id>', visited, name='visited'),
    path('posts/edit/<int:id>', edit, name='edit'),
    path('posts/delete/<int:id>', delete, name='delete'),
]
