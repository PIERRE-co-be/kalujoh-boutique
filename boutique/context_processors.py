from .models import Categorie

def menu_categories(request):
    return {
        'categories_menu': Categorie.objects.all()
    }