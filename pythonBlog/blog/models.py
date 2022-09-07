from django.db import models
from django.conf import settings

# Create your models here.
KATEGORIE = (('PYTHON','Python'),
            ('BIZNES','Biznes'),
            ('TECHNOLOGIE','Technologie'),
            ('POLITYKA','Polityka'),
            ('NAUKA PROGRAMOWANIA','Nauka Programowania'),
            ('NARZĘDZIA','Narzędzia'),
            ('INNE','Inne'))
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()

class Post (models.Model):
 
    autor = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tytul = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_modyfikacji = models.DateTimeField(auto_now=True)
    data_publikacji = models.DateTimeField(blank=True,null=True)
    czy_opublikowane = models.BooleanField(default=False)
    img = models.ImageField(upload_to='pictures',blank=True,null=True)
    kategorie = models.CharField(max_length=20,choices=KATEGORIE,default='INNE')

    class Meta:
        ordering = ['-data_publikacji']

    def __str__(self):
        return self.tytul

