from django.db import models

# Create your models here.
class Teacher(models.Model):
    name_teacher = models.CharField(
        max_length=255,
        verbose_name='Мугалимдин аты.'
    )
    image_teacher = models.ImageField(
        upload_to='teacher_image/',
        verbose_name='Мугалимдин суроту'
    )
    description_teacher = models.TextField(
        verbose_name='Мугалимдин кызматы.'
    )

    def __str__(self):
        return self.name_teacher

    class Meta:
        verbose_name = "Мугалимдер"
        verbose_name = "Мугалимдер"
        ordering = ('id', )