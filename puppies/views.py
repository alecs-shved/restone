#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import City, Street, Shops
from .serializers import CitySerializer, StreetSerializer, ShopsSerializer, ShopsallSerializer
from datetime import datetime, date, time
import json

# Create your views here.

@api_view(['GET', 'POST'])
def get_post_citys(request):
    # get all city. Pos a
    #curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/
    if request.method == 'GET':
        citys = City.objects.filter(name='Kupustin-Yar')
        serializer = CitySerializer(citys, many=True)
        return Response(serializer.data)
    # insert a new record for a city
    #curl  -v -X POST --data '{"name": "Kupustin-Yar"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/
    elif request.method == 'POST':
        data = {
           'name': request.data.get('name')
            }
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_street(request):
    # get all street to city. Pos b
    # curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/
    if request.method == 'GET':
        streets = Street.objects.filter()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    # insert a new record for a street
    #curl  -v -X POST --data '{"name":"Malina-street","city":1}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/
    elif request.method == 'POST':
        data = {
           'name': request.data.get('name'),
           'city': request.data.get('city'),
        }
        serializer = StreetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_shop(request):
    # get all street to city. Pos c
    # curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
    # curl  -v -X GET --data '{"name":"shop-six","city":"Kupustin-Yar","street":"Malina-street"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
    if request.method == 'GET':
        data = {
           'name': request.data.get('name'),
           'city': request.data.get('city'),
           'street': request.data.get('street'),
        }
        if data['city'] is not None:
            city = (City.objects.get(name=data['city'])).id
            data['city'] = city
        if data['street'] is not None:
                street = (Street.objects.get(name=data['street'])).id
                data['street'] = street
        datar = {}
        for dt in data:
            if data[dt] is not None:
                 datar[dt] = data[dt]        
        shop = Shops.objects.filter(**datar)
        lis = []
        for sh in shop:
            dic = {}
            dic['id'] = sh.id
            dic['name'] = sh.name
            dic['city'] = City.objects.get(id=Street.objects.get(id=sh.street_id).city_id)
            dic['street'] = Street.objects.get(id=sh.street_id)
            dic['home'] = sh.home
            dic['time_open'] = sh.time_open
            dic['time_close'] = sh.time_close
            now = datetime.now()
            d = date.today()
            open = datetime.strptime(str(d) + ' ' + sh.time_open, "%Y-%m-%d %H:%M")
            close = datetime.strptime(str(d) + ' ' + sh.time_close, "%Y-%m-%d %H:%M")
            if now > open and now < close:
                dic['open'] = 1
            else:
                dic['open'] = 0
            lis.append(dic)
        serializer = ShopsallSerializer(lis, many=True)
        return Response(serializer.data)
    # insert a new record for a street
    #curl  -v -X POST --data '{"name":"shop-six","city":1, "street":1, "home":14, "time_open":"08:00", "time_close":"20:00"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
    elif request.method == 'POST':
        data = {
           'name': request.data.get('name'),
           'city': request.data.get('city'),
           'street': request.data.get('street'),
           'home': request.data.get('home'),
           'time_open': request.data.get('time_open'),
           'time_close': request.data.get('time_close'),
        }
        serializer = ShopsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)