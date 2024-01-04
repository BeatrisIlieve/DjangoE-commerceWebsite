import os
from _decimal import Decimal
from collections import OrderedDict

import django
from django import forms

from django.db.models import Q, Count, F



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_commerce_website.settings")
django.setup()
from django.db import models

from e_commerce_website.shopping_cart.models import ShoppingCart
from e_commerce_website.jewelry.funcs import get_objects_pks
from django.utils.translation import gettext_lazy as _
from e_commerce_website.jewelry.models import (
    Category,
    GoldCaratWeight,
    Jewelry,
    Metal,
    Size,
    StoneColor,
    StoneType,
    JewelryMetal,
    JewelryStone
)

categories = Category.objects.all()
sizes = Size.objects.all()
names = Category.TitleChoices.names
values = Category.TitleChoices.values

# jewelries_pks = get_objects_pks(jewelries)
# stone_types_pks = StoneType.objects. \
#     prefetch_related('stone_types'). \
#     filter(jewelry__in=jewelries).values_list('id', flat=True)
#
# stone_colors_pks = StoneColor.objects. \
#     prefetch_related('stone_colors'). \
#     filter(jewelry__in=jewelries).values_list('id', flat=True)
#
# stone_types_pks = JewelryStone.objects.\
#     filter(
#     Q(jewelry_id__in=jewelries_pks) &
#     Q(stone_color_id__in=stone_colors_pks) &
#     Q(stone_type_id__in=stone_types_pks)).\
#     values_list('stone_type_id', flat=True)
#
# stone_colors_pks = JewelryStone.objects.\
#     filter(
#     Q(jewelry_id__in=jewelries_pks) &
#     Q(stone_color_id__in=stone_colors_pks) &
#     Q(stone_type_id__in=stone_types_pks)).\
#     values_list('stone_color_id', flat=True)
#
# stone_types = StoneType.objects.filter(id__in=stone_types_pks)
#
# stone_colors = StoneColor.objects.filter(id__in=stone_colors_pks)

jewelries = Jewelry.objects.filter(pk=6, stone_colors=1)
# stone_color = StoneColor.objects.\
#     prefetch_related('jewelry_set__stone_types').\
#     filter(jewelry__stone_types=1, jewelry__exact=6).values('stone_color_i')

stone_colors_cur = JewelryStone.objects.\
    filter(jewelry__in=[6], stone_type__exact=1).values_list('stone_color_id', flat=True)

stone_colors_pks = JewelryStone.objects. \
    filter(jewelry__in=[6], stone_type__exact=1). \
    values_list('stone_color_id', flat=True)

stone_colors = StoneColor.objects. \
    filter(id__in=[stone_colors_pks])

print(stone_colors)

stone_colors = StoneColor.objects. \
    prefetch_related('stone_colors'). \
    filter(jewelry__in=[6])

print(stone_colors)