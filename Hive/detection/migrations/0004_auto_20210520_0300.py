# Generated by Django 3.2.2 on 2021-05-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_auto_20210520_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='timeIn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movement',
            name='timeOut',
            field=models.DateField(blank=True, null=True),
        ),
    ]
