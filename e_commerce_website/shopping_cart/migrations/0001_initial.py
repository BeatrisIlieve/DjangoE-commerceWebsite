# Generated by Django 5.0 on 2024-01-09 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jewelry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('order_completed', models.BooleanField(default=False)),
                ('session_key', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewelry.jewelry')),
            ],
            options={
                'unique_together': {('session_key', 'jewelry')},
            },
        ),
    ]
