# Generated by Django 4.0.3 on 2022-04-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_travelform_dimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelform',
            name='dinfo',
            field=models.CharField(default='eat', max_length=1000),
            preserve_default=False,
        ),
    ]
