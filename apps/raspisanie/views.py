from django.shortcuts import render

from apps.raspisanie.models import Raspisanie

from apps.contacts.models import Contact

from apps.settings.models import Settings
# Create your views here.

def raspisanier(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    raspisanie = Raspisanie.objects.all()

    context = {
        'setting':setting,
        'contact':contact,
        'raspisanie':raspisanie,
    }
    
    return render(request, 'raspisanie.html', context)

def raspisanie_detail(request,id):
    raspisanie_new = Raspisanie.objects.all().order_by('?')

    raspisanie = Raspisanie.objects.get(id =id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
   
    context = {
        'setting':setting,
        'contact': contact,
        'raspisanie':raspisanie,
        'raspisanie_new':raspisanie_new,

    }

    return render(request, 'raspisanie_detail.html',context)