# Generated by Django 4.1.2 on 2022-10-31 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='Rating'),
        ),
    ]
