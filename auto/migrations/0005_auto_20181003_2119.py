# Generated by Django 2.1.1 on 2018-10-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_resultjs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultjs',
            name='errreason',
            field=models.CharField(max_length=500),
        ),
    ]
