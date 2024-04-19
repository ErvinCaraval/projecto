from rest_framework import serializers
from .models import Auction, Artwork, Customer, Bid, Admin

class AuctionSerializer(serializers.ModelSerializer):
     class Meta:
        model = Auction
        fields = '__all__'

class ArtworkSerializer(serializers.ModelSerializer):
     class Meta:
        model = Artwork
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
     class Meta:
        model = Customer
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
     class Meta:
        model = Bid
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
     class Meta:
        model = Admin
        fields = '__all__'
