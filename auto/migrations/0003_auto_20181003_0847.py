# Generated by Django 2.1.1 on 2018-10-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_auto_20181003_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultchart',
            name='etime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='resultchart',
            name='projectname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='resultchart',
            name='stime',
            field=models.CharField(max_length=20),
        ),
    ]