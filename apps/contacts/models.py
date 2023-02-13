from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_site = models.CharField(
        max_length=255,
        verbose_name='Телефон номер'
    )

    email_site = models.EmailField(
        max_length=255,
        verbose_name='Почта')

    location_site = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )

    facebook_site = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
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
