from django.http import HttpResponse
from django.shortcuts import render

from properties.models import Owner, Property


def property_list(request):
    p = Property.objects.all()
    return render(request, "properties/property_list.html", {"properties": p})


def owner_list(request):
    owners = Owner.objects.all()
    return render(request, "properties/owner_list.html", {"owners": owners})


def about(request):
    return HttpResponse("About")
