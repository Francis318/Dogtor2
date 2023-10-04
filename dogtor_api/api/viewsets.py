"""Rest API viewsets"""
from rest_framework import viewsets, decorators, response, permissions
from . import models, serializers


class UserViewSet(viewsets.ViewSet):
    serializer_class=serializers.UserModelSerializer
    def create(self, request):
        serializers=self.serializer_class(data=request.data)
        serializers.is_valid(raise_exeption=True)
        user=serializers.save()
        user.set_password(serializers.validated_data)
        return response.Response({"detail": f"user {user.username} created"}, status=201)


class OwnerViewSet(viewsets.ModelViewSet):
    """Owner viewset"""
    queryset= models.Owner.objects.all()
    serializer_class= serializers.OwnerModelSerializer
    #permission_classes=[permissions.IsAuthenticated]

    @decorators.action(detail=False, methods=["get"])
    def test(self, request):
        return response.Response({"message":"Listo"})

class SpeciesViewSet(viewsets.ModelViewSet):
    """Species viewset"""
    queryset= models.Species.objects.all()
    serializer_class= serializers.SpeciesModelSerializer

class PetViewSet(viewsets.ModelViewSet):
    """Pet viewset"""
    queryset= models.Pet.objects.all()
    serializer_class= serializers.PetModelSerializer	

class RecordViewSet(viewsets.ModelViewSet):
    """Record viewset"""
    queryset= models.Record.objects.all()
    serializer_class= serializers.RecordModelSerializer