# Generated by Django 3.2.9 on 2021-11-05 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0005_rename_user_user_c'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_c',
            old_name='usernanme',
            new_name='username',
        ),
    ]
