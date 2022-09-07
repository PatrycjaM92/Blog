from django.contrib import admin
from .models import Post,Profile

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id','tytul','autor','slug','data_utworzenia','data_publikacji')
    list_filter= ('data_utworzenia','data_publikacji')
    search_fields = ["tutul"]
        
        
    

admin.site.register(Profile)