from django.shortcuts import render

from apps.teacher.models import Teacher

from apps.contacts.models import Contact

from apps.settings.models import Settings

# Create your views here.

def teacher(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    teacher = Teacher.objects.all()
    
    context = {
        'setting':setting,
        'contact':contact,
        'teacher':teacher,
    }

    return render(request, 'teacher.html', context)