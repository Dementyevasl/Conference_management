# Generated by Django 2.2.1 on 2019-05-14 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0003_auto_20190514_0432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='linkedinid',
            new_name='linkedin',
        ),
    ]
