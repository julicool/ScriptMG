# Generated by Django 2.1.7 on 2019-02-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0020_remove_sys_dict_deploy_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileinfo',
            name='system_numb',
            field=models.CharField(max_length=10),
        ),
    ]
