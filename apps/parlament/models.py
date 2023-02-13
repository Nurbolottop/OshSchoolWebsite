from django.db import models

# Create your models here.
class Parlament(models.Model):
    name_teacher = models.CharField(
        max_length=255,
        verbose_name='Окуучунун  аты.'
    )
    image_teacher = models.ImageField(
        upload_to='teacher_image/',
        verbose_name='Окуучунун суроту'
    )
    description_teacher = models.TextField(
        verbose_name='Окуучунун кызматы.'
    )

    def __str__(self):
        return self.name_teacher

    class Meta:
        verbose_name = "Мектеп парламенти"
        verbose_name = "Мектеп парламенти"
        ordering = ('id', )