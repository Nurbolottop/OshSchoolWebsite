# Generated by Django 4.1.6 on 2023-02-13 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inst_akred', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acreditationlist1',
            options={'ordering': ('id',), 'verbose_name': 'Институциялдык аккредитация', 'verbose_name_plural': 'Институциялдык аккредитация'},
        ),
        migrations.AlterModelOptions(
            name='acreditationlist1detail',
            options={'ordering': ('id',), 'verbose_name': 'Институциялдык аккредитация болумго киргизуу', 'verbose_name_plural': 'Институциялдык аккредитация болумго киргизуу'},
        ),
    ]
