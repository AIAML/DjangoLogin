# Generated by Django 3.2.13 on 2022-06-08 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Logins', '0002_rename_login_loginmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loginmodel',
            new_name='Loginmodels',
        ),
    ]