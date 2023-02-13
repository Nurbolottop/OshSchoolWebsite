from django.shortcuts import render

from apps.students.models import Studet

from apps.contacts.models import Contact

from apps.settings.models import Settings

# Create your views here.

def students(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    students = Studet.objects.all()
    
    context = {
        'setting':setting,
        'contact':contact,
        'students':students,
    }

    return render(request, 'students.html', context)