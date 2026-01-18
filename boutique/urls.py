from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('categorie/<int:categorie_id>/', views.produits_par_categorie, name='produits_par_categorie'),
    path('produit/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    
    # Panier
    path('panier/ajouter/<int:produit_id>/', views.ajouter_panier, name='ajouter_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('panier/vider/', views.vider_panier, name='vider_panier'),
    
    # NOUVEAU : Modifier quantité et Supprimer un article spécifique
    path('panier/modifier/<str:item_id>/<str:action>/', views.modifier_quantite, name='modifier_quantite'),
    path('panier/supprimer/<str:item_id>/', views.supprimer_item, name='supprimer_item'),
]