from django.contrib import admin
from .models import Categorie, Produit, Publicite

# Personnalisation de l'affichage dans l'admin
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'tailles_dispo', 'date_ajout')
    search_fields = ('nom',)
    list_filter = ('categorie',)

class PubliciteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'active')

admin.site.register(Categorie)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Publicite, PubliciteAdmin)

# Changer le titre de l'interface admin
admin.site.site_header = "Administration KALUJOH"
admin.site.site_title = "KALUJOH Admin"