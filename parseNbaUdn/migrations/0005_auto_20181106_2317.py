# Generated by Django 2.1.3 on 2018-11-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parseNbaUdn', '0004_auto_20181106_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topnews',
            old_name='img',
            new_name='imgUrl',
        ),
    ]
