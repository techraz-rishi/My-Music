# Generated by Django 3.1.1 on 2020-09-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200918_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='category',
            field=models.CharField(choices=[('BR', 'Bollywood Romantic'), ('HR', 'Hollywood Romantic'), ('BRA', 'Bollywood Romantic Action'), ('BR', 'Bollywood Rock'), ('BNR', 'Bollywood Nineties 90s Romantic'), ('BER', 'Bollywood Eighties 80s Romantic'), ('BRUP', 'BreakUp Song'), ('BF', 'Best Friend'), ('FLR', 'First Love Romantic'), ('FS', 'Family Songs'), ('CH', 'Childhood Bachapan'), ('AGB', 'Anger Battle'), ('DD', 'Dancing DJ Rock'), ('LRH', 'Love Romantic Romance Heart'), ('BW', 'Bollywood'), ('HW', 'HollyWood'), ('VN', 'Valentine Love'), ('RG', 'Religious'), ('AR', 'Arties Bhajan'), ('DB', 'Patriotism Desh Bhakti DeshBhakti'), ('RAL', 'Revenge Anger Love'), ('RM', 'Romantic'), ('LV', 'Love')], max_length=5),
        ),
    ]