# Generated by Django 2.1.7 on 2019-02-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayaradz', '0003_auto_20190221_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeuser',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
