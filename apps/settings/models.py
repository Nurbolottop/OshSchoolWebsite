from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Settings(models.Model):
    name_site = models.CharField(
        max_length=244,
        verbose_name='Сайттын аты!'
    )
    logo_site = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo_site/',
        verbose_name='Мектептин логотиби'
    )
    description_site = models.TextField(
        verbose_name='Мектеп боюнча маалымат',
        blank=True,null=True
    )
    phone_site = models.CharField(
        max_length=255,
        verbose_name='Телефон номер',
        blank=True,null=True
    )
    email_site = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True,null=True
    )
    location_site = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,null=True
    )
    facebook_site = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True,
    )
    instagram_site = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    youtube_site = models.URLField(
        verbose_name='Youtube',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.name_site

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = "Настройка"

class Slide(models.Model):
    first_slide = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="slide_site/",
        verbose_name='Биринчи слайд'
    )
    second_slide = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
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
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to=255,
        verbose_name='Сурот'
    )
    class Meta:
        verbose_name = 'Сертификаттар'
        verbose_name_plural = 'Сертификаттар'
        ordering = ('id', )
        
class About(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to="About_image", 
        verbose_name="Сурот"
    )
    name = models.CharField(
        max_length=244, 
        verbose_name="Биз жонундо"
    )
    descriptions = models.TextField(
        verbose_name="Биз жонундо кошумча маалымат!"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Биз жонундо маалымат"
        verbose_name_plural = "Биз жонундо кошумча маалыматтар"
        ordering = ('id', )

class Lessons(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Сабакты аты"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="Сабактын жакшы отулгон пайызы"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Биздин сабак"
        verbose_name_plural = "Биздин сабактар"
        ordering = ('id', )

class Makal(models.Model):
    name = models.TextField(
        verbose_name="Макал"
    )
    description = models.CharField(
        max_length=255, 
        verbose_name="Макалдын автору"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Макалдар"
        verbose_name_plural = "Макалдар"
        ordering = ('id', )
        
class Pride(models.Model):
    image_pride = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_pride/',
        verbose_name="Суроту!"
    )
    name_pride = models.CharField(
        max_length=255,
        verbose_name='Сыймыктанабыз'
    )
    description_pride = models.TextField(
        verbose_name='Кошумча маалымат!'
    )
    def __str__(self):
        return self.name_pride

    class Meta:
        verbose_name = "Сыймыктанабыз!"
        verbose_name_plural = "Сыймыктанабыз!"
        ordering = ('id', )   
        
class News(models.Model):
    name_news = models.CharField(
        max_length= 255, 
        verbose_name='Название.'
    )
    image_news = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news_image/', 
        verbose_name='Фотография'
    )
    description_news = models.TextField(
        verbose_name='Описание'
    )
    created_news = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name_news

    class Meta:
        verbose_name = 'Жанылыктар'
        verbose_name_plural = 'Жанылыктар'
        ordering = ('id', )
        
class Contact(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name="Аты!"
        )
    email = models.EmailField(
        verbose_name='Почтасы'
        )
    message = models.TextField(
        verbose_name='Кабары'
        )

    def __str__(self):
        return f"Аты: {self.name}. Кабары: {self.message}"

    class Meta:
        verbose_name = 'Акыркы Кабарлар'
        verbose_name_plural = 'Акыркы Кабарлар'
        ordering = ('id', )
        
class Gallery(models.Model):
    
    gallery_image = models.ImageField(
        upload_to='gallery/', 
        verbose_name='Сурот'
        )
    
    def __str__(self):
        return f" {self.gallery_image}"
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        ordering = ('id', )