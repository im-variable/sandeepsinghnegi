# Generated by Django 3.2 on 2023-07-31 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authuserextenstion',
            old_name='user_id',
            new_name='user',
        ),
    ]
