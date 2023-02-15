from django.shortcuts import render
from apps.settings.models import Settings
from apps.parents.models import AchykSaat,Parents,Parlament,Student,Teacher

# Create your views here.
def parents(request):
    setting = Settings.objects.latest('id')
    parent = Parents.objects.all()
    context = {
        'setting':setting,
        'parent':parent,
    }
    return render(request, 'other_settings/parents.html', context)

def parlament(request):
    setting = Settings.objects.latest('id')
    parlament = Parlament.objects.all()
    context = {
        'setting':setting,
        'parlament':parlament,
    }
    return render(request, 'other_settings/parlament.html', context)

def students(request):
    setting = Settings.objects.latest('id')
    students = Student.objects.all()
    context = {
        'setting':setting,
        'students':students,
    }
    return render(request, 'other_settings/students.html', context)

def teacher(request):
    setting = Settings.objects.latest('id')
    teacher = Teacher.objects.all()
    context = {
        'setting':setting,
        'teacher':teacher,
    }
    return render(request, 'other_settings/teacher.html', context)

def achyksaat(request):
    achyksaat = AchykSaat.objects.all()
    setting = Settings.objects.latest('id')
    context = {
        'achyksaat':achyksaat,
        'setting':setting,
    }
    return render(request, 'other_settings/achyk_saat.html', context)

def achyksaat_detail(request,id):
    achyksaat = AchykSaat.objects.get(id = id)
    setting = Settings.objects.latest('id')
    context = {
        ''
        'achyksaat':achyksaat,
        'setting':setting,
    }
    return render(request, 'other_settings/achyk_detail.html', context)