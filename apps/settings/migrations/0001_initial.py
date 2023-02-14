# Generated by Django 4.1.6 on 2023-02-14 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About_image', verbose_name='Сурот')),
                ('name', models.CharField(max_length=244, verbose_name='Биз жонундо')),
                ('descriptions', models.TextField(verbose_name='Биз жонундо кошумча маалымат!')),
            ],
            options={
                'verbose_name': 'Биз жонундо маалымат',
                'verbose_name_plural': 'Биз жонундо кошумча маалыматтар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=255, verbose_name='Сурот')),
            ],
            options={
                'verbose_name': 'Сертификаттар',
                'verbose_name_plural': 'Сертификаттар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Аты!')),
                ('email', models.EmailField(max_length=254, verbose_name='Почтасы')),
                ('message', models.TextField(verbose_name='Кабары')),
            ],
            options={
                'verbose_name': 'Акыркы Кабарлар',
                'verbose_name_plural': 'Акыркы Кабарлар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_school', models.CharField(max_length=255, verbose_name='МЕКТЕПТИН НЕГИЗДЕЛГЕН ЖЫЛЫ')),
                ('child_school', models.CharField(max_length=255, verbose_name='ОКУУЧУЛАРДЫН САНЫ')),
                ('graduate_school', models.CharField(max_length=255, verbose_name='БҮТҮРҮҮЧҮЛӨР (ЖЫЛЫНА)')),
                ('book_school', models.CharField(max_length=255, verbose_name='КИТЕПТЕРДИН САНЫ')),
            ],
            options={
                'verbose_name': 'Биз сандабыз!',
                'verbose_name_plural': 'Биз сандабыз!',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Сабакты аты')),
                ('number', models.CharField(max_length=255, verbose_name='Сабактын жакшы отулгон пайызы')),
            ],
            options={
                'verbose_name': 'Биздин сабак',
                'verbose_name_plural': 'Биздин сабактар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Makal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Макал')),
                ('description', models.CharField(max_length=255, verbose_name='Макалдын автору')),
            ],
            options={
                'verbose_name': 'Макалдар',
                'verbose_name_plural': 'Макалдар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_news', models.CharField(max_length=255, verbose_name='Название.')),
                ('image_news', models.ImageField(upload_to='news_image/', verbose_name='Фотография')),
                ('description_news', models.TextField(verbose_name='Описание')),
                ('created_news', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Жанылыктар',
                'verbose_name_plural': 'Жанылыктар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Pride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_pride', models.ImageField(upload_to='image_pride/', verbose_name='Суроту!')),
                ('name_pride', models.CharField(max_length=255, verbose_name='Сыймыктанабыз')),
                ('description_pride', models.TextField(verbose_name='Кошумча маалымат!')),
            ],
            options={
                'verbose_name': 'Сыймыктанабыз!',
                'verbose_name_plural': 'Сыймыктанабыз!',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=244, verbose_name='Сайттын аты!')),
                ('logo_site', models.ImageField(upload_to='logo_site/', verbose_name='Мектептин логотиби')),
                ('description_site', models.TextField(blank=True, null=True, verbose_name='Мектеп боюнча маалымат')),
                ('phone_site', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон номер')),
                ('email_site', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('location_site', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('facebook_site', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram_site', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('youtube_site', models.URLField(blank=True, null=True, verbose_name='Youtube')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройка',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_slide', models.ImageField(upload_to='slide_site/', verbose_name='Биринчи слайд')),
                ('second_slide', models.ImageField(upload_to='slide_site/', verbose_name='Второй слайд')),
                ('description_slide', models.TextField(verbose_name='Слайдка маалымат!')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайд',
                'ordering': ('id',),
            },
        ),
    ]
