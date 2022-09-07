
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post,KATEGORIE

# Create your views here.

def home(request):
    return render(request,'blog/base.html')

# class PostList(generic.ListView):
#     queryset =Post.objects.all().order_by('-data_utworzenia')
#     template_name = 'blog/home.html'


# class PostDetail(generic.DetailView):
#     model= Post
#     template_name ='blog/post_detail.html'

def kategorylist():
    kat=[]
    for i in KATEGORIE:
        for j,val in enumerate(i):
            if j%2==1:
                kat.append(val)
    return kat
        

def postlist(request):
    posts=Post.objects.all().order_by('-data_utworzenia')
        
    return render(request,'blog/home.html',{'posts':posts})

def postdetail(request,slug):
    post = Post.objects.get(slug=slug)
    posts=Post.objects.all().order_by('-data_utworzenia')
    context = {
        'post': post,
        'posts':posts
    }
    return render(request, 'blog/post_detail.html', context)

def kategorie(request,kategorie):
    postskat = Post.objects.get(kategorie=kategorie)
    posts=Post.objects.all().order_by('-data_utworzenia')
    context = {
        'postkat': postskat,
        'posts':posts
    }
    return render(request,'blog/kategorie.html',context)

def oMnie(request):
    posts=Post.objects.all().order_by('-data_utworzenia')
    return  render(request,'blog/omnie.html',{'posts':posts})
