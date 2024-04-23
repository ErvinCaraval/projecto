from rest_framework import viewsets
from .serializer import AuctionSerializer, ArtworkSerializer, CustomerSerializer, BidSerializer, AdminSerializer
from .models import Auction, Artwork, Customer, Bid, Admin
from rest_framework.response import Response
from rest_framework import status

class CustomModelViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

    def perform_update(self, serializer):
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

    def perform_destroy(self, instance):
        if hasattr(instance, 'bid_set') and instance.bid_set.exists():
            return Response("No se puede eliminar este objeto porque tiene ofertas asociadas.", status=status.HTTP_400_BAD_REQUEST)
        
        if hasattr(instance, 'artwork_set') and instance.artwork_set.exists():
            return Response("No se puede eliminar este objeto porque tiene obras de arte asociadas.", status=status.HTTP_400_BAD_REQUEST)
        
        if hasattr(instance, 'admin_set') and instance.admin_set.exists():
            return Response("No se puede eliminar este objeto porque tiene administradores asociados.", status=status.HTTP_400_BAD_REQUEST)

        if hasattr(instance, 'bid_set') and instance.bid_set.exists():
            return Response("No se puede eliminar este objeto porque tiene ofertas asociadas.", status=status.HTTP_400_BAD_REQUEST)

        instance.delete()

class AuctionViewSet(CustomModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class ArtworkViewSet(CustomModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class CustomerViewSet(CustomModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class BidViewSet(CustomModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class AdminViewSet(CustomModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    
