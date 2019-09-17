
from django.contrib import admin
from django.urls import path
from test1 import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', local_views.hello_world),

    path('posts/', posts_views.list_posts),
]
