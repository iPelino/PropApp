from django.contrib import admin

from properties.models import (Address, Owner, Property, PropertyImage,
                               RentalAgreement, Tenant)

admin.site.register(Address)
admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(Tenant)
admin.site.register(RentalAgreement)
admin.site.register(PropertyImage)
