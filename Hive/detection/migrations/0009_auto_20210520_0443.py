# Generated by Django 3.2.2 on 2021-05-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0008_delete_movement'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='timeIn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='timeOut',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
