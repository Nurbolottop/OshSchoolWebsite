# Generated by Django 4.1.6 on 2023-02-15 10:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parlament',
            options={'ordering': ('id',), 'verbose_name': 'Мектеп парламенти', 'verbose_name_plural': 'Мектеп парламенти'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('id',), 'verbose_name': 'Класстар', 'verbose_name_plural': 'Класстар'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('id',), 'verbose_name': 'Мугалимдер', 'verbose_name_plural': 'Мугалимдер'},
        ),
        migrations.AlterField(
            model_name='parlament',
            name='image_teacher',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='teacher_image/', verbose_name='Окуучунун суроту'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image_student',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='student_image/', verbose_name='Класстын суроту'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image_teacher',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='teacher_image/', verbose_name='Мугалимдин суроту'),
        ),
    ]
