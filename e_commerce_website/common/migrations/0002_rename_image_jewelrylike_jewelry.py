# Generated by Django 5.0 on 2024-01-05 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jewelrylike',
            old_name='image',
            new_name='jewelry',
        ),
    ]
