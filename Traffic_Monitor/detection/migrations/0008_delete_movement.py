# Generated by Django 3.2.2 on 2021-05-20 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0007_remove_movement_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movement',
        ),
    ]
