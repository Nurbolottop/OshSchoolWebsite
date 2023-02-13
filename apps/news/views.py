from django.shortcuts import render

from apps.settings.models import Settings
from apps.news.models import News
from apps.contacts.models import Contact

# Create your views here.

def news(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    news = News.objects.all()

    context = {
        'setting':setting,
        'contact':contact,
        'news': news


    }

    return render(request, 'news.html', context)


def news_detail(request,id):
    random_new = News.objects.all().order_by('?')

    news = News.objects.get(id =id)
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
   
    context = {
        'setting':setting,
        'contact': contact,
        'news':news,
        'random_new':random_new,

    }

    return render(request, 'news-details.html',context)