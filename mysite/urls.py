from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    #Dashboard
    path('dashboard/', include('post.urls')),
    #Account
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    #Ckeditor
     path('ckeditor/', include('ckeditor_uploader.urls')),
]
