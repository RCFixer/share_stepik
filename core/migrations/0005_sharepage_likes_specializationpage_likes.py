# Generated by Django 4.2.5 on 2023-10-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_specializationpage_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharepage',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='specializationpage',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]