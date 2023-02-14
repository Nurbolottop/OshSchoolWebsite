from django.shortcuts import render
from apps.accreditational.models import Institutional_Accreditation,Program_Accreditation
from apps.settings.models import Settings

# Create your views here.
def main_accreditations(request):
    setting = Settings.objects.latest('id')
    context = {
        'setting':setting,
    }
    return render(request, 'accreditations/accred.html', context)

def institutional_accreditations(request):
    accreditation = Institutional_Accreditation.objects.all()
    setting = Settings.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
    }
    return render(request, 'accreditations/inst_akred.html', context)

def institutional_accreditations_detail(request,id):
    accreditation = Institutional_Accreditation.objects.get(id = id)
    setting = Settings.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
    }
    return render(request, 'accreditations/inst_detail.html', context)

def program_accreditation(request):
    accreditation = Program_Accreditation.objects.all()
    setting = Settings.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'setting':setting,
    }
    return render(request, 'accreditations/prog_akred.html', context)

def program_accreditation_detail(request,id):
    accreditation = Program_Accreditation.objects.get(id = id)
    setting = Settings.objects.latest('id')
    context = {
        ''
        'accreditation':accreditation,
        'setting':setting,
    }
    return render(request, 'accreditations/prog_detail.html', context)