from django.shortcuts import render
from apps.accreditational.models import Institutional_Accreditation,Program_Accreditation
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

def institutional_accreditations(request):
    accreditation = Institutional_Accreditation.objects.all()
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'inst_akred.html', context)

def institutional_accreditations_detail(request,id):
    accreditation = Institutional_Accreditation.objects.get(id = id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'inst_detail.html', context)

def accreditations2(request):
    accreditation = Program_Accreditation.objects.all()
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'prog_akred.html', context)

def accreditation_detail2(request,id):
    accreditation = Program_Accreditation.objects.get(id = id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'accreditation':accreditation,
        'setting':setting,
        'contact':contact
    }
    return render(request, 'prog_detail.html', context)