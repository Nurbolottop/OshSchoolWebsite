from django.db import models

# Create your models here.
class Raspisanie(models.Model):
    name = models.CharField(max_length= 255, verbose_name='Название.')
    image = models.ImageField(upload_to='raspisanie_image/', verbose_name='Фотография')
    created_raspisanie = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сабактардын жугуртмосу "
        verbose_name_plural = "Сабактардын жугуртмосу "
        ordering = ('id', )