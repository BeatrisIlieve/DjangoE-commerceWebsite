# Generated by Django 5.0 on 2023-12-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0004_alter_shoppingcart_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
