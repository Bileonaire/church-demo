# Generated by Django 2.1.4 on 2019-01-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='id_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
