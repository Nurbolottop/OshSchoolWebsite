from django.contrib import admin

from apps.achyk.models import AchykSaat, AchykSaatDetail

# Register your models here.
admin.site.register(AchykSaatDetail)
admin.site.register(AchykSaat)
