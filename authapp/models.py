from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    CHOICES = [
        ('Membre', 'Membre'),
        ('Banni', 'Banni'),
        ('Admin', 'Admin'),
    ]
    nom = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.nom
    
class Utilisateur(AbstractUser):
    pass 
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

class Article(models.Model):
    titre = models.CharField(max_length=100)
    texte = models.TextField()
    date = models.DateField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

