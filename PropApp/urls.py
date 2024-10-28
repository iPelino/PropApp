from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path

from properties.views import property_list, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("properties/", property_list),
    path("about", about),
] + debug_toolbar_urls()
