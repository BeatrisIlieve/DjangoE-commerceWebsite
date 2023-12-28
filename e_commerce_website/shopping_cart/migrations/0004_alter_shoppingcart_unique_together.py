# Generated by Django 5.0 on 2023-12-28 17:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0001_initial'),
        ('shopping_cart', '0003_remove_shoppingcart_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together={('user', 'jewelry')},
        ),
    ]
