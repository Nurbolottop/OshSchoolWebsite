from django.db import models

# Create your models here.
class Settings(models.Model):
    name_site = models.CharField(
        max_length=244,
        verbose_name='Сайттын аты!'
    )

    logo_site = models.ImageField(
        upload_to='logo_site/',
        verbose_name='Мектептин логотиби'
    )

    description_site = models.TextField(
        verbose_name='Мектеп боюнча маалымат'
    )

    def __str__(self):
        return self.name_site

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = "Настройка"

class Slide(models.Model):
    first_slide = models.ImageField(
        upload_to="slide_site/",
        verbose_name='Биринчи слайд'
    )
    second_slide = models.ImageField(
        upload_to='slide_site/',
        verbose_name='Второй слайд'
    )
    description_slide = models.TextField(
        verbose_name='Слайдка маалымат!'
    )

    def __str__(self):
        return self.description_slide

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайд"
        ordering = ('id', )

class Data(models.Model):
    years_school = models.CharField(
        max_length=255,
        verbose_name='МЕКТЕПТИН НЕГИЗДЕЛГЕН ЖЫЛЫ'
    )
    child_school = models.CharField(
        max_length=255,
        verbose_name="ОКУУЧУЛАРДЫН САНЫ"
    )
    graduate_school = models.CharField(
        max_length=255,
        verbose_name='БҮТҮРҮҮЧҮЛӨР (ЖЫЛЫНА)'

    )
    book_school = models.CharField(
        max_length=255,
        verbose_name='КИТЕПТЕРДИН САНЫ'
    )

    def __str__(self):
        return self.years_school

    class Meta:
        verbose_name = 'Биз сандабыз!'
        verbose_name_plural = 'Биз сандабыз!'
        ordering = ('id', )

class Certificate(models.Model):
    image = models.ImageField(
        upload_to=255,
        verbose_name='Сурот'
    )

    class Meta:
        verbose_name = 'Сертификаттар'
        verbose_name_plural = 'Сертификаттар'
        ordering = ('id', )