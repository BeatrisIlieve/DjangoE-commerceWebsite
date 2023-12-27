# Generated by Django 5.0 on 2023-12-27 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('B', 'Bracelets'), ('E', 'Earrings'), ('N', 'Necklaces'), ('R', 'Rings')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GoldCaratWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(choices=[('9', '9K'), ('10', '10K'), ('14', '14K'), ('18', '18K'), ('22', '22K')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Metal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('YG', 'Yellow Gold'), ('RG', 'Rose Gold'), ('WG', 'White Gold'), ('PT', 'Platinum')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='StoneColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('AQ', 'Aquamarine'), ('BL', 'Black'), ('BU', 'Blue'), ('GR', 'Green'), ('PI', 'Pink'), ('RE', 'Red'), ('WH', 'White'), ('YE', 'Yellow')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='StoneType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('BS', 'Black Spinel'), ('DI', 'Diamond'), ('EM', 'Emerald'), ('RU', 'Ruby'), ('SA', 'Sapphire')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_image_url', models.URLField()),
                ('second_image_url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry_category', to='jewelry.category')),
            ],
        ),
        migrations.CreateModel(
            name='JewelryMetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold_carat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jewelry_gold_carats', to='jewelry.goldcaratweight')),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry_metals', to='jewelry.jewelry')),
                ('metal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metals', to='jewelry.metal')),
            ],
            options={
                'unique_together': {('jewelry', 'metal', 'gold_carat')},
            },
        ),
        migrations.AddField(
            model_name='jewelry',
            name='gold_carats',
            field=models.ManyToManyField(through='jewelry.JewelryMetal', to='jewelry.goldcaratweight'),
        ),
        migrations.AddField(
            model_name='jewelry',
            name='metals',
            field=models.ManyToManyField(through='jewelry.JewelryMetal', to='jewelry.metal'),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.CharField(choices=[('1.00', '1.00 cm'), ('2.00', '2.00 cm'), ('3.00', '3.00 cm'), ('4.00', '4.00 cm'), ('5.00', '5.00 cm'), ('6.00', '6.00 cm'), ('7.00', '7.00 cm'), ('8.00', '8.00 cm'), ('9.00', '9.00 cm'), ('4.70', '4.70 cm'), ('4.80', '4.80 cm'), ('4.90', '4.90 cm'), ('5.05', '5.05 cm'), ('5.18', '5.18 cm'), ('5.30', '5.30 cm'), ('5.43', '5.43 cm'), ('5.56', '5.56 cm'), ('5.68', '5.68 cm'), ('5.81', '5.81 cm'), ('5.94', '5.94 cm'), ('6.07', '6.07 cm'), ('6.19', '6.19 cm'), ('15.20', '15.20 cm'), ('16.50', '16.50 cm'), ('17.80', '17.80 cm'), ('19.10', '19.10 cm'), ('20.30', '20.30 cm'), ('21.60', '21.60 cm'), ('40.64', '40.64 cm'), ('43.18', '43.18 cm'), ('45.72', '45.72 cm'), ('50.80', '50.80 cm'), ('55.88', '55.88 cm'), ('60.96', '60.96 cm'), ('81.28', '81.28 cm'), ('91.44', '91.44 cm'), ('182.88', '182.88 cm')], max_length=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size_category', to='jewelry.category')),
            ],
        ),
        migrations.CreateModel(
            name='JewelrySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry_sizes', to='jewelry.jewelry')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='jewelry.size')),
            ],
            options={
                'unique_together': {('jewelry', 'size')},
            },
        ),
        migrations.AddField(
            model_name='jewelry',
            name='size',
            field=models.ManyToManyField(through='jewelry.JewelrySize', to='jewelry.size'),
        ),
        migrations.CreateModel(
            name='JewelryStone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stone_carat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry_stones', to='jewelry.jewelry')),
                ('stone_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stone_colors', to='jewelry.stonecolor')),
                ('stone_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stone_types', to='jewelry.stonetype')),
            ],
            options={
                'unique_together': {('jewelry', 'stone_type', 'stone_color')},
            },
        ),
        migrations.AddField(
            model_name='jewelry',
            name='stone_colors',
            field=models.ManyToManyField(through='jewelry.JewelryStone', to='jewelry.stonecolor'),
        ),
        migrations.AddField(
            model_name='jewelry',
            name='stone_types',
            field=models.ManyToManyField(through='jewelry.JewelryStone', to='jewelry.stonetype'),
        ),
    ]
