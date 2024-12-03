from django.urls import path

from . import views

urlpatterns = [
    path("", views.property_list, name="property_list"),
    # properties/owners
    path("owners", views.owner_list, name="owner_list"),
]
