from django.core.management.base import BaseCommand

# import UserFactory here
from api.factories import UserFactory, ActivityFactory, UserWithActivityFactory

class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=10,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            UserWithActivityFactory.create()