# Generated by Django 4.0.3 on 2022-04-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='travelform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=30)),
                ('dimg', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='formcontact',
        ),
    ]
