
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from test1 import views as local_views
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.list_portfolio),
    path('hello/', local_views.hello_world, name="hello_word"),

    path('',include(('posts.urls','posts'),namespace='posts')),
    path('users/', include(('users.urls','users'),namespace='users')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
