from django.urls import path
from apps.accreditational.views import main_accreditations,institutional_accreditations,institutional_accreditations_detail,program_accreditation,program_accreditation_detail

urlpatterns = [
    path("main_accreditations/", main_accreditations, name= "main_accreditations"),
    path("institutional_accreditations/", institutional_accreditations, name= "institutional_accreditations"),
    path("institutional_accreditations_detail/<int:id>/", institutional_accreditations_detail, name= "institutional_accreditations_detail"),
    path("program_accreditation/", program_accreditation, name= "program_accreditation"),
    path("program_accreditation_detail/<int:id>/", program_accreditation_detail, name= "program_accreditation_detail"),
    
]