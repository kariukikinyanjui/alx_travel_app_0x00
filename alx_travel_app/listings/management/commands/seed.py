from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing


class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        # Create test host user
        host, created = User.objects.get_or_create(
            username='travelhost',
            defaults={
                'email': 'host@alxtravel.com',
                'password': 'hostpass123'
            }
        )
        if created:
            host.set_password('hostpass123')
            host.save()

        listings = [
            {
                "host": host,
                "title": "Cozy Cottage",
                "description": "A lovely cottage in the countryside.",
                "location": "Countryside",
                "price_per_night": 120.00,
                "available": True,
            },
            {
                "host": host,
                "title": "Luxury Apartment",
                "description": "A luxurious apartment in the city center.",
                "location": "City Center",
                "price_per_night": 250.00,
                "available": True,
            },
            {
                "host": host,
                "title": "Beach House",
                "description": "A beautiful house by the beach.",
                "location": "Beachfront",
                "price_per_night": 300.00,
                "available": True,
            },
        ]


        # Create listings
        for listing_data in listings:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults=listing_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Listing exists: {listing.title}'))
        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
