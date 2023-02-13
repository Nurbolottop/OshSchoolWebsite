"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from apps.prides.views import pride_detail
from apps.settings.views import index
from apps.news.views import news,news_detail
from apps.contacts.views import contact
from apps.teacher.views import teacher
from apps. inst_akred.views import accreditations1,accreditation_detail1

from apps. prog_akred.views import accreditations2,accreditation_detail2
from apps. accred.views import main_accreditations
from apps.parlament.views import parlament
from apps.parents.views import parents
from apps.students.views import students
from apps.raspisanie.views import raspisanier,raspisanie_detail
from apps.about.views import about
from apps.gallery.views import gallery,gallery_detail1
from apps.achyk.views import achyksaat, achyksaat_detail1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('pride_detail/<int:id>/', pride_detail, name="pride_detail"),
    path('news', news, name = "news"),
    path('news_detail/<int:id>/', news_detail, name='news_detail'),
    path('contact', contact, name = "contact"),
    path('teacher', teacher, name = "teacher"),
    path('institutsionaldyk-akkreditatsiya/', accreditations1, name='inst_akred'),    
    path('programmalyk-akkreditatsiya/', accreditations2, name='prog_akred'),
    path('main-akkreditatsiya/', main_accreditations, name='accred'),
    path('institutsionaldyk-akkreditatsiya_detail/<int:id>/', accreditation_detail1, name = 'inst_detail' ),
    path('programmalyk-akkreditatsiya_detail/<int:id>/', accreditation_detail2, name = 'prog_detail' ),

    path('parlament', parlament, name = "parlament"),
    path('parents/', parents, name = "parents"),
    path('students/', students, name = "students"),
    path('raspisanie', raspisanier, name = "raspisanie"),
    path('raspisanie_detail/<int:id>/', raspisanie_detail, name='raspisanie_detail'),
    path('about', about, name = "about"),
    path('gallery', gallery, name = "gallery"),
    path('gallery_detail/<int:id>/', gallery_detail1, name = 'gallery_detail' ),
    path('achykl-saat/', achyksaat, name='achyk_saat'),    
    path('achykl-saat_detail/<int:id>/', achyksaat_detail1, name = 'achyk_detail' ),
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)