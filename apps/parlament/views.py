from django.shortcuts import render

from apps.parlament.models import Parlament

from apps.contacts.models import Contact

from apps.settings.models import Settings

# Create your views here.

def parlament(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    parlament = Parlament.objects.all()
    
    context = {
        'setting':setting,
        'contact':contact,
        'parlament':parlament,
    }

    return render(request, 'parlament.html', context)