from django.shortcuts import render

from apps.prog_akred.models import AcreditationList2
from apps.settings.models import Settings
from apps.contacts.models import Contact
# Create your views here.
def accreditations2(request):
    accreditation = AcreditationList2.objects.all()
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'prog_akred.html', context)

def accreditation_detail2(request,id):
    accreditation = AcreditationList2.objects.get(id = id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'prog_detail.html', context)