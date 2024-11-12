from django.urls import path

from core.views import test_view, example, ProductList, product_list

urlpatterns =[
    path("", test_view), # localhost:8000/test/example
    path("example", example),
    path("products", ProductList.as_view()),
    path("product-list", product_list),

]