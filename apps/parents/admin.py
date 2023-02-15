from django.contrib import admin
from apps.parents.models import Parents,Parlament,Student,AchykSaat,AchykSaatDetail,Teacher

# Register your models here.
admin.site.register(Parents)
admin.site.register(Parlament)
admin.site.register(Student)
admin.site.register(AchykSaatDetail)
admin.site.register(AchykSaat)
admin.site.register(Teacher)
