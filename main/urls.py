from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruta/', include('app01.urls')),
    path('livros/', include('app02.urls')),
    path('produtos/', include('cadastroP.urls')),
    path('cadastro/', include('cadastroUser.urls')),
    path('login/', include('login.urls')),
]
