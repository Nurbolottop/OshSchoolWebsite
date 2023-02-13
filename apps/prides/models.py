from django.db import models

# Create your models here.
class Pride(models.Model):
    image_pride = models.ImageField(
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