from django.shortcuts import render

from apps.inst_akred.models import AcreditationList1
from apps.settings.models import Settings
from apps.contacts.models import Contact
# Create your views here.
def accreditations1(request):
    accreditation = AcreditationList1.objects.all()
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'inst_akred.html', context)

def accreditation_detail1(request,id):
    accreditation = AcreditationList1.objects.get(id = id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'inst_detail.html', context)