from django.shortcuts import render

from apps.achyk.models import AchykSaat
from apps.settings.models import Settings
from apps.contacts.models import Contact
# Create your views here.
def achyksaat(request):
    achyksaat = AchykSaat.objects.all()
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'achyksaat':achyksaat,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'achyk_saat.html', context)

def achyksaat_detail1(request,id):
    achyksaat = AchykSaat.objects.get(id = id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'achyksaat':achyksaat,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'achyk_detail.html', context)