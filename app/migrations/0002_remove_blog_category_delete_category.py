# Generated by Django 4.0.1 on 2022-01-20 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
