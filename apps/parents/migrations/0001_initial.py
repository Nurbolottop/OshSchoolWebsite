# Generated by Django 4.1.3 on 2022-12-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244, verbose_name='Суроо!')),
                ('desc', models.TextField(verbose_name='Жоор!')),
            ],
            options={
                'verbose_name': 'Ата энелерге!',
                'verbose_name_plural': 'Ата эненлерге',
            },
        ),
    ]