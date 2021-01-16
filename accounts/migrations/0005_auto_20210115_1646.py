# Generated by Django 3.1.5 on 2021-01-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AddField(
            model_name='user',
            name='user_types',
            field=models.CharField(default='', max_length=1000000),
            preserve_default=False,
        ),
    ]
