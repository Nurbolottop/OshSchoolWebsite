from django.urls import path
from apps.parents.views import parents,parlament,students,teacher,achyksaat,achyksaat_detail

urlpatterns = [
    path("parents/", parents, name= "parents"),
    path("parlament/", parlament, name= "parlament"),
    path("students/", students, name= "students"),
    path("teacher/", teacher, name= "teacher"),
    path("achyksaat/", achyksaat, name= "achyksaat"),
    path("achyksaat_detail/<int:id>/", achyksaat_detail, name= "achyksaat_detail"),
]