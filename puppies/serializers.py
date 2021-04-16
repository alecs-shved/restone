from rest_framework import serializers
from .models import City, Street, Shops_all

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('name','city',)

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops_all
        fields = ('name','city','street','home','date_open','date_close')