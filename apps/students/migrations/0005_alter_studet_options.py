# Generated by Django 4.1.6 on 2023-02-13 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_studet_desc_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studet',
            options={'ordering': ('id',), 'verbose_name': 'Класстар'},
        ),
    ]
