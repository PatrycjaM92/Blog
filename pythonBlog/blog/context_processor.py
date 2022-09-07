import imp
from .models import Post

def postlist(request):
    posts=Post.objects.all().order_by('-data_utworzenia')
    return {'posts':posts}