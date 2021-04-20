from django.db import models

# Create your models here.

CITYS = (
    'Roston-on-Don',
    'Volgograd',
    'Tumbov',
    )
STREETS = (
    'Sudovaya-street',
    'Nugibina-street',
    'Pogodina-street',
    )
SHOPS = (
    'Shop-one',
    'Shop-two',
    'Shop-three',
    )

class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
       return self.name
    
    def get_breed(self):
        return self.name + ' belongs to '

    def __repr__(self):
        return self.name + ' is added.'

class Street(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):
       return self.name

    def get_breed(self):
        return self.name + ' belongs to '

    def __repr__(self):
        return self.name + ' is added.'

class Shops(models.Model):
    name = models.CharField(max_length=30)
    city = models.IntegerField(default=0)
    street = models.ForeignKey(Street, on_delete = models.CASCADE)
    home = models.IntegerField(default=1)
    time_open = models.CharField(max_length=15)
    time_close = models.CharField(max_length=15)

class Shops_all(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    home = models.IntegerField(default=1)
    time_open = models.CharField(max_length=15)
    time_close = models.CharField(max_length=15)