# Generated by Django 3.1.7 on 2021-02-22 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]