# Generated by Django 4.1.5 on 2023-01-11 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_customeruser_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='password2',
        ),
    ]
