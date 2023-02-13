from django.db import models

# Create your models here.
class Contact(models.Model):
    

    def __str__(self):
        return self.phone_site

    class Meta:
        verbose_name = "Контакттар"
        verbose_name_plural = "Контакттар"
        ordering = ('id', )


class Comment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Аты!")
    email = models.EmailField(verbose_name='Почтасы')
    message = models.TextField(verbose_name='Кабары')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акыркы Кабарлар'
        verbose_name_plural = 'Акыркы Кабарлар'
        ordering = ('id', )
