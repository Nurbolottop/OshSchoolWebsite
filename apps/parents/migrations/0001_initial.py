# Generated by Django 4.1.6 on 2023-02-14 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AchykSaat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
            ],
            options={
                'verbose_name': 'Ачык саат',
                'verbose_name_plural': 'Ачык саат',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244, verbose_name='Аты!')),
                ('parents_doc', models.FileField(upload_to='parents_document/', verbose_name='Документ файл')),
            ],
            options={
                'verbose_name': 'Ата энелерге!',
                'verbose_name_plural': 'Ата эненлерге',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Parlament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_teacher', models.CharField(max_length=255, verbose_name='Окуучунун  аты.')),
                ('image_teacher', models.ImageField(upload_to='teacher_image/', verbose_name='Окуучунун суроту')),
                ('description_teacher', models.TextField(verbose_name='Окуучунун кызматы.')),
            ],
            options={
                'verbose_name': 'Мектеп парламенти',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=255, verbose_name='Класстын аты.')),
                ('image_student', models.ImageField(upload_to='student_image/', verbose_name='Класстын суроту')),
            ],
            options={
                'verbose_name': 'Класстар',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_teacher', models.CharField(max_length=255, verbose_name='Мугалимдин аты.')),
                ('image_teacher', models.ImageField(upload_to='teacher_image/', verbose_name='Мугалимдин суроту')),
                ('description_teacher', models.TextField(verbose_name='Мугалимдин кызматы.')),
            ],
            options={
                'verbose_name': 'Мугалимдер',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='AchykSaatDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achyksaat', models.FileField(upload_to='achyksaat/', verbose_name='Документ файл')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
                ('accreditation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achyksaat', to='parents.achyksaat', verbose_name='Ачык саат')),
            ],
            options={
                'verbose_name': 'Ачык саат болумго киргизуу',
                'verbose_name_plural': 'Ачык саат болумго киргизуу',
                'ordering': ('id',),
            },
        ),
    ]
