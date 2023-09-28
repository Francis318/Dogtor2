from django.urls import path, include
from rest_framework import routers
from . import viewsets


router= routers.DefaultRouter()
router.register(r'owners', viewsets.OwnerViewSet)
router.register(r'species', viewsets.SpeciesViewSet)
router.register(r'pets', viewsets.PetViewSet)


urlpatterns=[
    path("", include(router.urls))
]