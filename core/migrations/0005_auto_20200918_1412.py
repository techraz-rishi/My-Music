# Generated by Django 3.1.1 on 2020-09-18 08:42

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200918_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='audioFile1s/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_image',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='images/'),
        ),
    ]