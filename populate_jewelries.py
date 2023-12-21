import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_commerce_website.settings")
django.setup()

from e_commerce_website.jewelry.models import (
    Jewelry,
    JewelryMetal,
    JewelryStone,
)

from get_all_objects import (
    categories,
    jewelries,
    metals,
    gold_carats,
    stone_types,
    stone_colors
)


def bulk_create_jewelry(*args):
    Jewelry.objects.bulk_create(*args)


bulk_create_jewelry(
    [
        Jewelry(
            title='Chandelier',
            quantity=10,
            price=120000.00,
            first_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703167483/earrings/1/diamond_chandelier_earrings.webp',
            second_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703167483/earrings/1/diamond_chandelier_earrings_eadpchsmct.webp',
            category=categories[1],
        ),

        Jewelry(
            title='Queen of Diamonds',
            quantity=10,
            price=163000.00,
            first_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703168853/earrings/2/diamond_chandelier_earrings_eadpclafrchaa.webp',
            second_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703168594/earrings/2/diamond_chandelier_earrings_eadpclafrcha.webp',
            category=categories[1],
        ),

        Jewelry(
            title='Garland Heart',
            quantity=10,
            price=32000.00,
            first_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703175666/earrings/3/garland_earrings_diamond_eadphssmoc_581447_e-1_ysmxop.webp',
            second_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703175667/earrings/3/garland_earrings_diamond_eadphssmoc_581447_e-2_z74pjd.webp',
            category=categories[1],
        ),

        Jewelry(
            title='Pirouette',
            quantity=10,
            price=24000.00,
            first_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703176025/earrings/4/pirouette_earrings__diamond__eadprfprspir_e-1_zfcw3e.webp',
            second_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703176029/earrings/4/pirouette_earrings__diamond__eadprfprspir_e-2_qafrue.webp',
            category=categories[1],
        ),

        Jewelry(
            title='Lotus Cluster',
            quantity=10,
            price=56000.00,
            first_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703177862/earrings/5/lotus_cluster_earrings_diamond_eadpde010ltc_e-1_dstqna.webp',
            second_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703177862/earrings/5/lotus_cluster_earrings_diamond_eadpde010ltc_e-2_cd7sd2.webp',
            category=categories[1],
        ),

        Jewelry(
            title='Classics',
            quantity=10,
            price=97000.00,
            first_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703178293/earrings/6/drop_earrings_diamond_and_ruby_earmrpsfpsd_431958_e-1_cycchy.webp',
            second_image_url='https://res.cloudinary.com/deztgvefu/image/upload/v1703178292/earrings/6/drop_earrings_diamond_and_ruby_earmrpsfpsd_431958_e-2_gs6ai0.webp',
            category=categories[1],
        ),

    ]
)


def bulk_create_jewelry_by_metal(*args):
    JewelryMetal.objects.bulk_create(*args)


bulk_create_jewelry_by_metal(
    [
        JewelryMetal(
            jewelry=jewelries[0],
            metal=metals[3],
        ),

        JewelryMetal(
            jewelry=jewelries[1],
            metal=metals[3],
        ),

        JewelryMetal(
            jewelry=jewelries[2],
            metal=metals[3],
        ),

        JewelryMetal(
            jewelry=jewelries[3],
            metal=metals[3],
        ),

        JewelryMetal(
            jewelry=jewelries[4],
            metal=metals[3],
        ),

        JewelryMetal(
            jewelry=jewelries[5],
            metal=metals[3],
        ),

        JewelryMetal(
            jewelry=jewelries[5],
            metal=metals[0],
            gold_carat=gold_carats[3]
        ),

    ]
)


def bulk_create_jewelry_by_stone(*args):
    JewelryStone.objects.bulk_create(*args)


bulk_create_jewelry_by_stone(
    [
        JewelryStone(
            jewelry=jewelries[0],
            stone_type=stone_types[7],
            stone_color=stone_colors[0],
            stone_carat=16.81,
        ),

        JewelryStone(
            jewelry=jewelries[1],
            stone_type=stone_types[7],
            stone_color=stone_colors[0],
            stone_carat=9.21,
        ),

        JewelryStone(
            jewelry=jewelries[2],
            stone_type=stone_types[7],
            stone_color=stone_colors[0],
            stone_carat=2.05,
        ),

        JewelryStone(
            jewelry=jewelries[3],
            stone_type=stone_types[7],
            stone_color=stone_colors[0],
            stone_carat=4.52,
        ),

        JewelryStone(
            jewelry=jewelries[4],
            stone_type=stone_types[7],
            stone_color=stone_colors[0],
            stone_carat=4.30,
        ),

        JewelryStone(
            jewelry=jewelries[5],
            stone_type=stone_types[7],
            stone_color=stone_colors[0],
            stone_carat=2.91,
        ),

        JewelryStone(
            jewelry=jewelries[5],
            stone_type=stone_types[7],
            stone_color=stone_colors[20],
            stone_carat=2.03,
        ),
    ]

)
