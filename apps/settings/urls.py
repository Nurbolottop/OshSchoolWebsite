from django.urls import path
from apps.settings.views import index,about,pride_detail,news,news_detail,contact,gallery

urlpatterns = [
    path("", index, name= "index"),
    path("about/", about, name= "about"),
    path("pride_detail/<int:id>/", pride_detail, name= "pride_detail"),
    path("news/", news, name= "news"),
    path("news_detail/<int:id>/", news_detail, name= "news_detail"),
    path("contact/", contact, name= "contact"),
    path("gallery/", gallery, name= "gallery"),
]