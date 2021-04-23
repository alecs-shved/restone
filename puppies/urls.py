from django.urls import path
from . import views


urlpatterns = [
    path(
        'city/',
        views.get_post_citys,
        name='get_post_citys'
    ),
    path(
        'city/street/',
        views.get_post_street,
        name='get_post_street'
    ),
    path(
        'shop/',
        views.get_post_shopz,
        name='get_post_shopz'
    ),
    path('shop/<str:street_type>', 
          views.get_post_shopz, 
          name='get_post_shopz'),
   ]