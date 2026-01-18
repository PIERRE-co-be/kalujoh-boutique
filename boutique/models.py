from django.db import models

# 1. Table pour les Catégories (Filles, Garçons, Femmes)
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.nom

# 2. Table pour les Publicités (Bannières)
class Publicite(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pubs/')
    lien = models.URLField(blank=True, null=True, help_text="Lien optionnel vers un produit")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

# 3. Table pour les Vêtements (SANS PRIX)
class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='produits/')
    description = models.TextField(blank=True)
    
    # Gestion des tailles et couleurs
    tailles_dispo = models.CharField(max_length=200, help_text="Ex: S, M, L, XL ou 2 ans, 4 ans")
    couleurs_dispo = models.CharField(max_length=200, help_text="Ex: Rouge, Bleu, Jaune, Motif Fleurs")
    
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom