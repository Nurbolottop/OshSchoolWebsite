from django.shortcuts import render

from apps.gallery.models import Gallery
from apps.settings.models import Settings
from apps.contacts.models import Contact
# Create your views here.
def gallery(request):
    gallery = Gallery.objects.all()
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'gallery':gallery,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'gallery.html', context)

def gallery_detail1(request,id):
    gallery = Gallery.objects.get(id = id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'gallery':gallery,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'gallery_detail.html', context)