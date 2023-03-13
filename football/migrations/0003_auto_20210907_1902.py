# Generated by Django 3.2.6 on 2021-09-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_auto_20210809_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='stadium',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
    ]
