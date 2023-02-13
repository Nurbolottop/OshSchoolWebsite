from django.shortcuts import render


from apps.settings.models import Settings
from apps.contacts.models import Contact
from apps.about.models import About,Lessons,Makal
from apps.settings.models import Data

# Create your views here.


def about(request):
    about = About.objects.latest('id')
    data = Data.objects.latest('id')
    lesson = Lessons.objects.all()
    makal = Makal.objects.all()

    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'about':about,
        'setting':setting,
        'contact':contact,
        'lesson':lesson,
        'makal':makal,

        'data':data
    }
    return render(request, 'about.html', context)