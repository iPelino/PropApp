from django.http import HttpResponse
from django.shortcuts import render

from properties.models import Property


def property_list(request):
    p = Property.objects.all()
    return render(request,
                  "properties/property_list.html",
                  {"properties": p})

def testview():
    pass


def about(request):
    return HttpResponse("About")
