from django.contrib import admin
from django.urls import path
from contact import views as contact_views

urlpatterns = [
    
    path('kontakt/', contact_views.contact_view, name='kontakt'),
]
