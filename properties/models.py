from django.db import models

property_types = (
    ("commercial", "commercial"),
    ("residential", "residential"),
    ("warehouse", "warehouse"),
    ("apartment", "apartment"),
)


class Address(models.Model):
    street = models.CharField(max_length=200)
    town = models.CharField(max_length=100)
    house_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}-{self.house_number}-{self.town}"


class Property(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=property_types)
    rooms = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 9999999.99
    owner = models.ManyToManyField("Owner", related_name="properties")

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name

    # list residential properties
    @staticmethod
    def list_residential_properties():
        return Property.objects.filter(type="residential")


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="properties/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.property.name


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class RentalAgreement(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)  # 9999999.99
    contact_file = models.FileField(upload_to="agreements/", null=True, blank=True)

    def __str__(self):
        return self.property.name
