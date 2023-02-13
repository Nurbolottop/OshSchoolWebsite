from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contact
# Create your views here.

def main_accreditations(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'setting':setting,
        'contact': contact
    }
    return render(request, 'accred.html', context)