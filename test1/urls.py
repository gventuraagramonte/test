
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from test1 import views as local_views
from posts import views as posts_views
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.list_portfolio),
    path('hello/', local_views.hello_world),

    path('posts/', posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
