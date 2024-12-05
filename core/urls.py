from django.urls import path

from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("products", views.ProductList.as_view()),
    path("product-list", views.product_list),
]
