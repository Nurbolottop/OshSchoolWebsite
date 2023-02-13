from django.db import models
from django_cleanup import cleanup

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

    @property
    def compressed_file_size(self):
        return self.parents_doc.size

    def save(self, *args, **kwargs):
        # автоматически сжимаем файл перед сохранением
        cleanup(self, 'parents_doc')
        super().save(*args, **kwargs)
        
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

class Student(models.Model):
    name_student = models.CharField(
        max_length=255,
        verbose_name='Класстын аты.'
    )
    image_student = models.ImageField(
        upload_to='student_image/',
        verbose_name='Класстын суроту'
    )

    def __str__(self):
        return self.name_student

    class Meta:
        verbose_name = "Класстар"
        verbose_name = "Класстар"
        ordering = ('id', )
        
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