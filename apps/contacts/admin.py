from django.contrib import admin

from apps.contacts.models import Contact, Comment
# Create your views here.
admin.site.register(Contact)
admin.site.register(Comment)
