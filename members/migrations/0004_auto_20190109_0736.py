# Generated by Django 2.1.4 on 2019-01-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20190104_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
