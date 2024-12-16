from django.db import models

# Create your models here.
from django.db import models

class Candidat(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Recruteur(models.Model):
    nom_entreprise = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nom_entreprise
