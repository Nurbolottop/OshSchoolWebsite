from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Parents(models.Model):
    name = models.CharField(
        max_length=244, 
        verbose_name='Аты!'
        )
    parents_doc = models.FileField(
        upload_to='parents_document/', 
        verbose_name='Документ файл'
        )
        
    def __str__(self):
        return f"{self.name} - {self.parents_doc}"

    class Meta:
        verbose_name = "Ата энелерге!"
        verbose_name_plural = "Ата эненлерге"
        ordering = ('id', )
        
class Parlament(models.Model):
    name_teacher = models.CharField(
        max_length=255,
        verbose_name='Окуучунун  аты.'
    )
    image_teacher = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
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
        verbose_name_plural = "Мектеп парламенти"
        ordering = ('id', )

class Student(models.Model):
    name_student = models.CharField(
        max_length=255,
        verbose_name='Класстын аты.'
    )
    image_student = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='student_image/',
        verbose_name='Класстын суроту'
    )

    def __str__(self):
        return self.name_student

    class Meta:
        verbose_name = "Класстар"
        verbose_name_plural = "Класстар"
        ordering = ('id', )
        
class Teacher(models.Model):
    name_teacher = models.CharField(
        max_length=255,
        verbose_name='Мугалимдин аты.'
    )
    image_teacher = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
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
        verbose_name_plural = "Мугалимдер"
        ordering = ('id', )
        
# Create your models here.
class AchykSaat(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ачык саат'
        verbose_name_plural = 'Ачык саат'
        ordering = ('id', )

class AchykSaatDetail(models.Model):
    accreditation = models.ForeignKey(
        AchykSaat,
        on_delete= models.CASCADE,
        related_name="achyksaat",
        verbose_name="Ачык саат"
    )
    achyksaat = models.FileField(
        upload_to='achyksaat/', 
        verbose_name='Документ файл'
        )
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ачык саат болумго киргизуу'
        verbose_name_plural = 'Ачык саат болумго киргизуу'
        ordering = ('id', )