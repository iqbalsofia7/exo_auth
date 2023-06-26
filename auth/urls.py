"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authapp.views import * 
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# from authapp.views import CustomLoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home ,name='home'),
    path('create/article', createArticle ,name='createA'),
    path('create/role', createRole ,name='createR'),
    path('create/utilisateur', createUtilisateur ,name='createU'),

    path('deconnexion/', LogoutView.as_view(next_page='home'), name='deco'),
    path('connexion/', CustomLoginView.as_view(), name='connexion'),
    path('change-password/', PasswordChangeView.as_view(success_url=reverse_lazy('home')), name='change_password'),
    # path('connexion/', connexion, name='connexion'),
    # path('deconnexion/', deco, name='deco'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)