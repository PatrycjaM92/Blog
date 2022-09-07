
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,'blog/base.html')

# class PostList(generic.ListView):
#     queryset =Post.objects.all().order_by('-data_utworzenia')
#     template_name = 'blog/home.html'


# class PostDetail(generic.DetailView):
#     model= Post
#     template_name ='blog/post_detail.html'


        

def postlist(request):
    search_post = request.GET.get('search')
    if search_post:  
        posts = Post.objects.filter(Q(tytul__icontains=search_post) & Q(tresc__icontains=search_post))
    else:
        posts=Post.objects.all().order_by('-data_utworzenia')
        
    return render(request,'blog/home.html',{'posts':posts})

def postdetail(request,slug):
    post = Post.objects.get(slug=slug)
   
    context = {
        'post': post
        
    }
    return render(request, 'blog/post_detail.html', context)

def postByKat(request,kategoria):
    posts = Post.objects.filter(kategoria=kategoria)
    return render(request,'blog/kategorie.html',{'posts':posts})

