# Generated by Django 3.1.1 on 2020-09-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200918_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to='audioFiles/'),
        ),
    ]
