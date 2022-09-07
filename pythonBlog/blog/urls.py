from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('',views.PostList.as_view(),name='home'),
    # path('<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),
    path('',views.postlist,name='post_list'),
    path('post/<slug>/', views.postdetail, name = 'post_detail'),
    #path('o_mnie/',views.oMnie,name='omnie'),
    path('o_mnie/',TemplateView.as_view(template_name="blog/omnie.html"),name="omnie")
    
   
    
    
    ]