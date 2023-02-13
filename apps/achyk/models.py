from django.db import models

# Create your models here.
class AchykSaat(models.Model):
    name = models.CharField(max_length=255, verbose_name='Аты')

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
    achyksaat = models.FileField(upload_to='achyksaat/', verbose_name='Документ файл')
    name = models.CharField(max_length=255, verbose_name='Аты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ачык саат болумго киргизуу'
        verbose_name_plural = 'Ачык саат болумго киргизуу'
        ordering = ('id', )