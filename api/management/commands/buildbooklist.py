import os
import json

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Read the folders and files in static/audio and generate or update the index file for the API'

    def handle(self, *args, **options):
        root = settings.AUDIOBOOKS_ROOT
        listings_filename = settings.AUDIOBOOKS_LISTING_FILE

        with open(listings_filename, 'r') as listing_file:
            listings_data = json.loads(listing_file.read())

        for book_dir in os.listdir(root):
            if book_dir not in listings_data:
                data = {
                    'title': book_dir,
                    'album_art': '{0}.jpg'.format(book_dir),
                    'description': None,
                    'parts': []
                }

                for filename in os.listdir(os.path.join(root, book_dir)):
                    data['parts'].append({'title': filename, 'description': None, 'file': filename})
                
                listings_data[book_dir] = data

        with open(listings_filename, 'w') as listing_file:
            listing_file.write(json.dumps(listings_data, indent=4, sort_keys=True))
