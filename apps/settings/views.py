from django.shortcuts import render,redirect
from apps.settings.models import Settings,Contact,About,Slide,Data,Certificate,Lessons,Makal,Pride,News, Gallery
from django.core.mail import send_mail

# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    pride = Pride.objects.all()
    data = Data.objects.latest('id')
    certificate = Certificate.objects.all()
    news = News.objects.all()
    context = {
        'setting':setting,
        'slide':slide,
        'pride':pride,
        'data':data,
        'certificate':certificate,
        'news': news
    }
    return render(request, 'settings/index.html', context)

def about(request):
    about = About.objects.latest('id')
    data = Data.objects.latest('id')
    lesson = Lessons.objects.all()
    makal = Makal.objects.all()
    setting = Settings.objects.latest('id')
    context = {
        'about':about,
        'setting':setting,
        'lesson':lesson,
        'makal':makal,
        'data':data
    }
    return render(request, 'settings/about.html', context)

def pride_detail(request,id):
    setting = Settings.objects.latest('id')
    pride = Pride.objects.get(id =id)
    context = {
        'setting':setting,
        'pride':pride,
    }
    return render(request, 'settings/course-details.html', context)

def news(request):
    setting = Settings.objects.latest('id')
    news = News.objects.all()
    context = {
        'setting':setting,
        'news': news
    }
    return render(request, 'settings/news.html', context)

def news_detail(request,id):
    random_new = News.objects.all().order_by('?')
    news = News.objects.get(id =id)
    setting = Settings.objects.latest('id')
    context = {
        'setting':setting,
        'news':news,
        'random_new':random_new,
    }
    return render(request, 'settings/news-details.html',context)

def contact(request):
    setting = Settings.objects.latest('id')
    if request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name = name, email = email, message = message)
        send_mail(
            f'{message}',
            f'Саламатсызбы {name}, калтырган кабарынызга ыраазычылык билдиребиз. Биз сиз менен жакынкы убакта кабарлашабыз, сураныч байланышта болунуз. Сиздин кабарыныз: {message}, сиздин почтаныз: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
    context = {
        'setting':setting,
    }
    return render(request, 'settings/contact.html', context)

def gallery(request):
    setting = Settings.objects.latest('id')
    gallery = Gallery.objects.all()
    context = {
        'setting':setting,
        'gallery': gallery
    }
    return render(request, 'settings/gallery.html', context)

def gallery_detail(request,id):
    gallery = Gallery.objects.get(id =id)
    setting = Settings.objects.latest('id')
    context = {
        'setting':setting,
        'gallery':gallery,
    }
    return render(request, 'settings/gallery_detail.html',context)