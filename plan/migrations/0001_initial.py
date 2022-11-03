# Generated by Django 4.1.2 on 2022-10-30 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Plan name')),
                ('desc', models.CharField(max_length=250, verbose_name='Description')),
                ('price', models.CharField(max_length=50, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('points', models.IntegerField(verbose_name='Total Points')),
                ('duration', models.PositiveIntegerField(verbose_name='Duration')),
                ('duration_mode', models.CharField(choices=[('M', 'Months'), ('D', 'Days'), ('W', 'Weeks'), ('Y', 'Years')], max_length=1, verbose_name='Duration mode')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=255, verbose_name='Benefit Details')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan', verbose_name='Plan')),
            ],
            options={
                'verbose_name': 'Benefit',
                'verbose_name_plural': 'Benefits',
            },
        ),
    ]
