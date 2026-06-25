from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('shop/', shop, name='shop'),
    path("customers/", customer_list, name="customer_list"),
    path("customers/create/", customer_create, name="customer_create"),
    path("customers/update/<int:id>/", customer_update, name="customer_update"),
    path("customers/delete/<int:id>/", customer_delete, name="customer_delete"),

    path("categories/create/", category_create, name="category_create"),
    path("categories/update/<int:id>/", category_update, name="category_update"),
    path("categories/delete/<int:id>/", category_delete, name="category_delete"),

    path("products/create/", product_create, name="product_create"),
    path("products/update/<int:id>/", product_update, name="product_update"),
    path("products/delete/<int:id>/", product_delete, name="product_delete"),

    path("orders/", order_list, name="order_list"),
    path("orders/create/", order_create, name="order_create"),
    path("orders/update/<int:id>/", order_update, name="order_update"),
    path("orders/delete/<int:id>/", order_delete, name="order_delete"),


    path("order-items/", order_item_list, name="order_item_list"),
    path("order-items/create/", order_item_create, name="order_item_create"),
    path("order-items/update/<int:id>/", order_item_update, name="order_item_update"),
    path("order-items/delete/<int:id>/", order_item_delete, name="order_item_delete"),
]