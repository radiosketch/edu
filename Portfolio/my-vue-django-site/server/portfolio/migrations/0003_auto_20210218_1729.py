# Generated by Django 2.2 on 2021-02-18 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='date',
        ),
    ]
