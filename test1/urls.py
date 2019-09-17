
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hola mundo desde Yacachay!!!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world)
]
