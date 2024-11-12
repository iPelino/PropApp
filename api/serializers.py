from rest_framework import serializers

from properties.models import Owner, Property, Tenant, Address


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','first_name', 'last_name', 'email', 'phone_number']
        extra_kwargs = {
            'id': {'read_only': True},
            # 'last_name': {'write_only': True},
        }


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'town', 'house_number']
        extra_kwargs = {
            'id': {'read_only': True},
        }

class PropertySerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=True)
    class Meta:
        model = Property
        fields = ['id', 'name', 'type', 'rooms', 'available', 'address', 'price', 'owner']

        extra_kwargs = {
            'id': {'read_only': True},
            # 'owner': {'required': False},
        }

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        prop = Property.objects.create(**validated_data)
        for owner in owner_data:
            Owner.objects.create(property=prop, **owner)
        return prop


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']
        extra_kwargs = {
            'id': {'read_only': True},
        }


# class