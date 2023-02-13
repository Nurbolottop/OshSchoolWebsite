from django.db import models

# Create your models here.
class News(models.Model):
    name_news = models.CharField(max_length= 255, verbose_name='Название.')
    image_news = models.ImageField(upload_to='news_image/', verbose_name='Фотография')
    description_news = models.TextField(verbose_name='Описание')
    created_news = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_news

    class Meta:
        verbose_name = 'Жанылыктар'
        verbose_name_plural = 'Жанылыктар'
        ordering = ('id', )