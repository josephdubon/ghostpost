# Generated by Django 3.1.7 on 2021-02-22 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0002_auto_20210222_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='boasts',
            new_name='boasts',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='roasts',
            new_name='roast',
        ),
    ]