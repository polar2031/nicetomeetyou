# Generated by Django 2.1.3 on 2018-11-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parseNbaUdn', '0005_auto_20181106_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topnews',
            name='postId',
            field=models.IntegerField(),
        ),
    ]
