# Generated by Django 2.1.7 on 2019-02-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0010_userlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='authorizations',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
