from django.shortcuts import render,redirect
from apps.settings.models import Settings,Slide,Data,Certificate,About,Lessons,Makal,Pride,News,Contact
from django.core.mail import send_mail

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

def pride_detail(request,id):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    pride = Pride.objects.get(id =id)
    context = {
        'setting':setting,
        'contact':contact,
        'pride':pride,
    }
    return render(request, 'course-details.html', context)

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
    return render(request, 'contact.html', context)