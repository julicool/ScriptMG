# Generated by Django 2.1.1 on 2018-10-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0006_resultjs_stime'),
    ]

    operations = [
        migrations.CreateModel(
            name='timejob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stime', models.CharField(max_length=20)),
                ('pjname', models.CharField(max_length=20)),
            ],
        ),
    ]
