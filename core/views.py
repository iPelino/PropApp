from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.forms import ContactForm
from core.models import Product
from core.serializers import ProductSerializer
from properties.models import Property


def home(request):
    query = request.GET.get("q")
    if query:
        properties = Property.objects.filter(
            Q(name__icontains=query)
            | Q(type__icontains=query)
            | Q(address__town__icontains=query)
        ).prefetch_related("images")
        # print(properties)
    else:
        properties = Property.objects.prefetch_related("images").all()

    return render(request, "home.html", {"properties": properties})


def test_view(request):
    return HttpResponse("Test view")


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # handle form errors
            pass
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
