# Generated by Django 3.1.5 on 2021-01-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='betausers',
            name='company',
            field=models.CharField(default='', max_length=180),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='betausers',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
