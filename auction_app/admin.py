from django.contrib import admin
from .models import Auction, Artwork, Customer, Bid, Admin

admin.site.register(Auction)
admin.site.register(Artwork)
admin.site.register(Customer)
admin.site.register(Bid)
admin.site.register(Admin)