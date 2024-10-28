from django.urls import path

from api.views import owner_list, properties

urlpatterns = [
    path('owners/', owner_list),
    path('properties/', properties),
]