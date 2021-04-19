import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import City, Street
from ..serializers import CitySerializer

# initialize the APIClient app

client = Client()

class GetAllCityTest(TestCase):
    """ Test module for GET all city API """
    def setUp(self):
        City.objects.create(
            name='Kupustin-Yar',)
        City.objects.create(
            name='Astrahan',)
    def test_get_post_citys(self):
        # get API response
        response = client.get(reverse('get_post_citys'))
        # get data from db
        citys = City.objects.filter(name='Kupustin-Yar')
        serializer = CitySerializer(citys, many=True)
        print(citys)
        print(response.data)
        print(serializer.data)
        print(response.status_code)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

'''class CreateNewCityTest(TestCase):
    """ Test module for inserting a new puppy """
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
        }
        self.invalid_payload = {
            'name': '',
        }
    def test_create_valid_city(self):
        response = client.post(
            reverse('get_post_citys'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_citys'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)'''


'''class GetAllStreetTest(TestCase):
    """ Test module for GET all puppies API """
    def setUp(self):
        City.objects.create(
            name='Casper',)
        Street.objects.create(
            name='Casper', city_id=1)
    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_street'))
        print('shved')
        # get data from db
        puppies = Street.objects.all()
        serializer = StreetSerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)'''