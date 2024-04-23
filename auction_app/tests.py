from django.test import TestCase
from .models import Auction, Artwork, Customer, Bid, Admin

class ModelTests(TestCase):
    def test_models(self):
        # Crear instancias de cada modelo
        auction = Auction.objects.create(auction_name="Subasta de prueba", auction_description="Descripción de la subasta", start_date="2024-04-30 12:00:00", end_date="2024-05-01 12:00:00", status="active")
        artwork = Artwork.objects.create(auction=auction, title="Obra de arte de prueba", artist="Artista de prueba", year_created=2020, dimensions="10x10", material="Material de prueba", genre="Género de prueba", description="Descripción de la obra de arte de prueba", minimum_bid=10.00, status="active")
        customer = Customer.objects.create(full_name="Cliente de prueba", email="cliente@example.com", phone="123456789", document_type="Tipo de documento", document_number="12345678")
        bid = Bid.objects.create(auction=auction, artwork=artwork, customer=customer, bid_value=15.00, bid_timestamp="2024-04-30 13:00:00")
        admin = Admin.objects.create(email="admin@example.com", password="password")

        # Aserciones simples para verificar que se hayan creado instancias de cada modelo
        self.assertEqual(Auction.objects.count(), 1)
        self.assertEqual(Artwork.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Bid.objects.count(), 1)
        self.assertEqual(Admin.objects.count(), 1)

