# Generated by Django 3.1.5 on 2021-01-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210116_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ManyToManyField(to='accounts.UserType', verbose_name='User Type'),
        ),
    ]
