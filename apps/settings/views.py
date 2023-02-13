from django.shortcuts import render

from apps.settings.models import Settings,Slide,Data,Certificate
from apps.prides.models import Pride
from apps.news.models import News
from apps.contacts.models import Contact

# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    slide = Slide.objects.latest('id')
    pride = Pride.objects.all()
    data = Data.objects.latest('id')
    certificate = Certificate.objects.all()
    news = News.objects.all()

    context = {
        'setting':setting,
        'contact':contact,
        'slide':slide,
        'pride':pride,
        'data':data,
        'certificate':certificate,
        'news': news


    }

    return render(request, 'index.html', context)