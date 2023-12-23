from django.urls import path

from e_commerce_website.jewelry.views import show_jewelry_details, DisplayJewelriesView

urlpatterns = (
    # path("<int:category_id>/", display_jewelries, name="show_jewelries"),
    path("<int:category_id>/", DisplayJewelriesView.as_view(), name="show_jewelries"),
    path("<int:category_id>/<int:jewelry_id>/", show_jewelry_details, name='show_jewelry_details')
)
