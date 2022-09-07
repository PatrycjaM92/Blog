from django.shortcuts import render
from contact.forms import ContactForm
from .forms import ContactForm
from blog.models import Post

# Create your views here.


def contact_view(request):
  
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/success.html')
    form = ContactForm()
    context = {'form': form,
               
               }
    return render(request, 'blog/kontakt.html', context)

    