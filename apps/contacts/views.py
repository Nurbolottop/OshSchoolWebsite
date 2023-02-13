from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.settings.models import Settings
from apps.contacts.models import Contact,Comment

# Create your views here.

def contact(request):
    setting = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')

    if request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Comment.objects.create(name = name, email = email, message = message)

        send_mail(
            f'{message}',
            f'Саламатсызбы {name}, калтырган кабарынызга ыраазычылык билдиребиз. Биз сиз менен жакынкы убакта кабарлашабыз, сураныч байланышта болунуз. Сиздин кабарыныз: {message}, сиздин почтаныз: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')

    context = {
        'setting':setting,
        'contact':contact,


    }

    return render(request, 'contact.html', context)

