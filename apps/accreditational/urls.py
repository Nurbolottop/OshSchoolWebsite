from django.urls import path
from apps.accreditational.views import main_accreditations,institutional_accreditations,institutional_accreditations_detail
urlpatterns = [
    path("main_accreditations/", main_accreditations, name= "main_accreditations"),
    path("institutional_accreditations/", institutional_accreditations, name= "institutional_accreditations"),
    path("institutional_accreditations_detail/", institutional_accreditations_detail, name= "institutional_accreditations_detail"),
]