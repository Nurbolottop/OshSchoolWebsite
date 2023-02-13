from django.contrib import admin

from apps.gallery.models import GalleryDetail, Gallery


# Register your models here.

admin.site.register(Gallery)
admin.site.register(GalleryDetail)