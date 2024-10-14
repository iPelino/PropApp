from django.contrib import admin

from properties.models import Address, Owner, Tenant, RentalAgreement, Property

admin.site.register(Address)
admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(Tenant)
admin.site.register(RentalAgreement)

