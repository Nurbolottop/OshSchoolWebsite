from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to="About_image", verbose_name="Сурот")
    name = models.CharField(max_length=244, verbose_name="Биз жонундо")
    descriptions = models.TextField(verbose_name="Биз жонундо кошумча маалымат!")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Биз жонундо маалымат"
        verbose_name_plural = "Биз жонундо кошумча маалыматтар"
        ordering = ('id', )

class Lessons(models.Model):
    name = models.CharField(max_length=255,verbose_name="Сабакты аты")
    number = models.CharField(max_length=255,verbose_name="Сабактын жакшы отулгон пайызы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Биздин сабак"
        verbose_name_plural = "Биздин сабактар"
        ordering = ('id', )

class Makal(models.Model):
    name = models.TextField(verbose_name="Макал")
    description = models.CharField(max_length=255, verbose_name="Макалдын автору")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Макалдар"
        verbose_name_plural = "Макалдар"
        ordering = ('id', )