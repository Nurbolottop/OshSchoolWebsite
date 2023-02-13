from django.shortcuts import render

from apps.contacts.models import Contact

from apps.settings.models import Settings
from apps.prides.models import Pride

# Create your views here.

def pride_detail(request,id):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    pride = Pride.objects.get(id =id)
    
    context = {
        'setting':setting,
        'contact':contact,
        'pride':pride,


    }

    return render(request, 'course-details.html', context)