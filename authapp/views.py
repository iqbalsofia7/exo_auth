from django.shortcuts import render, redirect
from .models import Utilisateur, Article, Role
from .forms import RegisterForm, ArticleForm, RoleForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import random

def home(request):
    user = request.user
    articles = Article.objects.all()
    return render(request, 'auth/front/index.html', {'user':user, "articles":articles} )

def createRole(request):
    if request.method == 'POST':
        form = RoleForm(request.POST) #class
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoleForm()
    return render(request, 'auth/back/create/createRole.html', {'form':form})

@login_required(login_url='connexion')
def createArticle(request):
    user = request.user

    if request.method == 'POST':
        form = ArticleForm(request.POST) #class
        if form.is_valid():
            article = form.save(commit=False)
            article.utilisateur = user
            article.save()
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
        form.current_user = user
    return render(request, 'auth/back/create/createArticle.html', {'form':form})


def createUtilisateur(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) #class
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])

            roles = Role.objects.all()
            random_role = random.choice(roles)
            user.role = random_role

            user.save()
            form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm ()
    return render(request, 'auth/back/create/createUtilisateur.html', {'form':form})


class CustomLoginView(LoginView):
    template_name = 'auth/front/connexion.html'  # Chemin vers le template de connexion
    redirect_authenticated_user = True  # Redirige les utilisateurs déjà connectés

    def get_success_url(self):
        return reverse_lazy('home')  # Redirige vers l'URL souhaitée après la connexion réussie
