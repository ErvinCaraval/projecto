from django.urls import path, include  # Corregir la importación

from rest_framework import routers
from auction_app import views

router = routers.DefaultRouter()
router.register(r'Auction', views.AuctionViewSet)
router.register(r'Artwork', views.ArtworkViewSet)
router.register(r'Customer', views.CustomerViewSet)
router.register(r'Bid', views.BidViewSet)
router.register(r'Admin', views.AdminViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

    


