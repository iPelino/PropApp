from rest_framework import serializers

from properties.models import Owner, Property


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','first_name', 'last_name', 'email', 'phone_number']
        extra_kwargs = {
            'id': {'read_only': True},
            # 'last_name': {'write_only': True},
        }


class PropertySerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=True)
    class Meta:
        model = Property
        fields = ['id', 'name', 'type', 'rooms', 'available', 'address', 'price', 'owner']