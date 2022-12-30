from .views import ifsc_search
from django.urls import include, path

from rest_framework import routers


urlpatterns = [

    path('ifsc/', ifsc_search, name='ifsc'),

]
