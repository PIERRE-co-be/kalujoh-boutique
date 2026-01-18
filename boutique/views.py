from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Publicite, Categorie

# Accueil et Détail (Inchangé)
def accueil(request):
    pubs = Publicite.objects.filter(active=True)
    produits = Produit.objects.all().order_by('-date_ajout')
    return render(request, 'boutique/accueil.html', {'pubs': pubs, 'produits': produits})

def produits_par_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    produits = Produit.objects.filter(categorie=categorie).order_by('-date_ajout')
    return render(request, 'boutique/accueil.html', {'produits': produits, 'titre_page': categorie.nom})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    similaires = Produit.objects.filter(categorie=produit.categorie).exclude(pk=produit_id)[:4]
    tailles = [t.strip() for t in produit.tailles_dispo.split(',')]
    couleurs = [c.strip() for c in produit.couleurs_dispo.split(',')]
    return render(request, 'boutique/detail.html', {'produit': produit, 'similaires': similaires, 'tailles': tailles, 'couleurs': couleurs})

# --- LOGIQUE PANIER AMÉLIORÉE ---

def ajouter_panier(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Produit, pk=produit_id)
        taille = request.POST.get('taille')
        couleur = request.POST.get('couleur')
        item_id = f"{produit_id}-{taille}-{couleur}"
        
        panier = request.session.get('panier', {})

        if item_id in panier:
            panier[item_id]['quantite'] += 1
        else:
            panier[item_id] = {
                'nom': produit.nom,
                'taille': taille,
                'couleur': couleur,
                'quantite': 1,
                'image': produit.image.url,
                # On ajoute l'URL absolue pour WhatsApp (utile lors de l'hébergement)
                'full_image_url': request.build_absolute_uri(produit.image.url) 
            }
        
        request.session['panier'] = panier
        
        # ICI LE CHANGEMENT : On reste sur la page précédente au lieu d'aller au panier
        return redirect(request.META.get('HTTP_REFERER', 'accueil'))
    
    return redirect('accueil')

def modifier_quantite(request, item_id, action):
    panier = request.session.get('panier', {})
    
    if item_id in panier:
        if action == 'plus':
            panier[item_id]['quantite'] += 1
        elif action == 'moins':
            panier[item_id]['quantite'] -= 1
            if panier[item_id]['quantite'] < 1:
                del panier[item_id] # Supprime si quantité devient 0
    
    request.session['panier'] = panier
    return redirect('voir_panier')

def supprimer_item(request, item_id):
    panier = request.session.get('panier', {})
    if item_id in panier:
        del panier[item_id]
    request.session['panier'] = panier
    return redirect('voir_panier')

def voir_panier(request):
    panier = request.session.get('panier', {})
    return render(request, 'boutique/panier.html', {'panier': panier})

def vider_panier(request):
    request.session['panier'] = {}
    return redirect('accueil')