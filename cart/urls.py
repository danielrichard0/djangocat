from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path("", views.insert_cart, name="cart-insert" ),
    path("cart-component/", views.get_cart_component, name="select-cart-component"),
    path("cart-update-overall", views.update_cart_overall, name="update-cart-overall"),
    path('get-quantity', views.get_quantity,name="get-quantity"),
    path("delete-item/", views.delete_item, name="delete-item"),
    path("lihat-keranjang", views.select_cart, name="select-cart"),
    path("change-quantity", views.change_quantity, name="change-quantity")
]
