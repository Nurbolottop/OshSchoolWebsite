from django.db import models
from django_cleanup import cleanup

# Create your models here.
class Institutional_Accreditation(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Институциялдык аккредитация'
        verbose_name_plural = 'Институциялдык аккредитация'
        ordering = ('id', )


class Institutional_Accreditation_Detail(models.Model):
    accreditation = models.ForeignKey(
        Institutional_Accreditation,
        on_delete= models.CASCADE,
        related_name="accreditation",
        verbose_name="Аккредитация"
    )
    accreditation_detail = models.FileField(
        upload_to='accreditation/', 
        verbose_name='Документ файл'
        )
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
        )

    @property
    def compressed_file_size(self):
        return self.accreditation_detail.size

    def save(self, *args, **kwargs):
        # автоматически сжимаем файл перед сохранением
        cleanup(self, 'accreditation_detail')
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name} - {self.accreditation_detail}"

    class Meta:
        verbose_name = 'Институциялдык аккредитация болумго киргизуу'
        verbose_name_plural = 'Институциялдык аккредитация болумго киргизуу'
        ordering = ('id', )
        
class Program_Accreditation(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программалык аккредитация'
        verbose_name_plural = 'Программалык аккредитация'
        ordering = ('id', )

class Program_Accreditation_Detail(models.Model):
    accreditation = models.ForeignKey(
        Program_Accreditation,
        on_delete= models.CASCADE,
        related_name="accreditation",
        verbose_name="Аккредитация"
    )
    accreditation_detail = models.FileField(
        upload_to='accreditation/', 
        verbose_name='Документ файл'
        )
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
        )
    @property
    def compressed_file_size(self):
        return self.accreditation_detail.size

    def save(self, *args, **kwargs):
        # автоматически сжимаем файл перед сохранением
        cleanup(self, 'accreditation_detail')
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.name} - {self.accreditation_detail}"


    class Meta:
        verbose_name = 'Программалык аккредитация болумго киргизуу'
        verbose_name_plural = 'Программалык аккредитация болумго киргизуу'
        ordering = ('id', )