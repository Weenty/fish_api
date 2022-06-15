from django.core.management.base import BaseCommand
from fish_api.factory import *
class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--all', type=int, help='Number of fake records for the database')



    def handle(self, *args, **options):
        if options['all']:
            for _ in range(options['all']):
                BoatFactory.create()
                PositionsFactory.create()
            
            for _ in range(options['all']):
                PlaceFishingFactory.create()

            for _ in range(options['all']):
                PersonFactory.create()
                BanFactory.create()
                CatchFactory.create()

            for _ in range(options['all']):
               FlightFactory.create()

            for _ in range(options['all']):
                FlightHasPersonFactory.create()
                FlightHasBanFactory.create()
                FlightHasCatchFactory.create()