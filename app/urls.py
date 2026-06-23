from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('/shop', shop, name='shop'),
    path("customers/", customer_list, name="customer_list"),
    path("customers/create/", customer_create, name="customer_create"),
    path("customers/update/<int:pk>/", customer_update, name="customer_update"),
    path("customers/delete/<int:pk>/", customer_delete, name="customer_delete"),

    path("categories/", category_list, name="category_list"),
    path("categories/create/", category_create, name="category_create"),
    path("categories/update/<int:pk>/", category_update, name="category_update"),
    path("categories/delete/<int:pk>/", category_delete, name="category_delete"),

    path("products/", product_list, name="product_list"),
    path("products/create/", product_create, name="product_create"),
    path("products/update/<int:pk>/", product_update, name="product_update"),
    path("products/delete/<int:pk>/", product_delete, name="product_delete"),

    path("orders/", order_list, name="order_list"),
    path("orders/create/", order_create, name="order_create"),
    path("orders/update/<int:pk>/", order_update, name="order_update"),
    path("orders/delete/<int:pk>/", order_delete, name="order_delete"),


    path("order-items/", order_item_list, name="order_item_list"),
    path("order-items/create/", order_item_create, name="order_item_create"),
    path("order-items/update/<int:pk>/", order_item_update, name="order_item_update"),
    path("order-items/delete/<int:pk>/", order_item_delete, name="order_item_delete"),
]