from rest_framework import viewsets
from .serializer import AuctionSerializer, ArtworkSerializer, CustomerSerializer, BidSerializer, AdminSerializer
from .models import Auction, Artwork, Customer, Bid, Admin

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']   