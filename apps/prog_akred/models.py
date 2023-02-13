from django.db import models

# Create your models here.
class AcreditationList2(models.Model):
    name = models.CharField(max_length=255, verbose_name='Аты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программалык аккредитация'
        verbose_name_plural = 'Программалык аккредитация'
        ordering = ('id', )

class AcreditationList2Detail(models.Model):
    accreditation = models.ForeignKey(
        AcreditationList2,
        on_delete= models.CASCADE,
        related_name="accreditation",
        verbose_name="Аккредитация"
    )
    accreditation_detail = models.FileField(upload_to='accreditation/', verbose_name='Документ файл')
    name = models.CharField(max_length=255, verbose_name='Аты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программалык аккредитация болумго киргизуу'
        verbose_name_plural = 'Программалык аккредитация болумго киргизуу'
        ordering = ('id', )