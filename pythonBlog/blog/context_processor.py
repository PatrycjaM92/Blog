import imp
from .models import Post,Kategorie

def postlist(request):
    posts=Post.objects.all().order_by('-data_utworzenia')
    return {'posts':posts}

def kategorie_widok(request):
    
    kategorie = Kategorie.objects.all()
    return {'kategorie':kategorie}