from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=255, verbose_name='Аты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея '
        verbose_name_plural = 'Галерея'
        ordering = ('id', )


class GalleryDetail(models.Model):
    accreditation = models.ForeignKey(
        Gallery,
        on_delete= models.CASCADE,
        related_name="gallery",
        verbose_name="Галерея"

    )
    gallery_image = models.ImageField(upload_to='gallery/', verbose_name='Сурот')
    

    class Meta:
        verbose_name = 'Галерея  болумго киргизуу'
        verbose_name_plural = 'Галерея  болумго киргизуу'
        ordering = ('id', )