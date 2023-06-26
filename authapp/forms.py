from django import forms
from .models import Article, Role, Utilisateur

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['utilisateur']
    def save(self, commit=True):
        article = super(ArticleForm, self).save(commit=False)
        article.utilisateur = self.current_user
        if commit:
            article.save()
        return article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['utilisateur']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Utilisateur
        fields = ['username', 'password', 'email', 'first_name', 'last_name']