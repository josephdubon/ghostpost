# Generated by Django 3.1.7 on 2021-02-22 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0003_auto_20210222_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_roast',
            field=models.BooleanField(default=False),
        ),
    ]
