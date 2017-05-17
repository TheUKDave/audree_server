import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import JsonResponse


class JSONGetView(View):
    """
    A basic class-based view that can be used to render a JSON response.
    """

    http_method_names = ['get', 'head', 'options', 'trace']

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """

        return JsonResponse(context, **response_kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_data(*args, **kwargs)
        return self.render_to_response(context)

    def get_data(self, context):
        """
        Override in the inheriting class to get a python object to serialize
        """

        raise NotImplemented


class BookList(JSONGetView):

    def get_data(self):
        listings_filename = settings.AUDIOBOOKS_LISTING_FILE

        with open(listings_filename, 'r') as listing_file:
            listings_data = json.loads(listing_file.read())

        data = {}
        for key, value in listings_data.items():
            data[key] = {
                'title': value['title'],
                'url': reverse('api:chapters', args=[key]),
                'art': static("{0}/{1}".format(settings.ALBUM_ART_DIRNAME, value['album_art']))
            }
            if value['description'] is not None:
                data[key]['description'] = value['description']

        return data


class ChapterList(JSONGetView):

    def get_data(self, slug):
        listings_filename = settings.AUDIOBOOKS_LISTING_FILE

        with open(listings_filename, 'r') as listing_file:
            listings_data = json.loads(listing_file.read())

        book_data = listings_data[slug]
        chapters = []

        for chapter in book_data['parts']:
            chapter_data = {
                'title': chapter['title'],
                'url': static("{0}/{1}/{2}".format(settings.AUDIOBOOKS_DIRNAME, slug, chapter['file'])),
            }

            if chapter['description'] is not None:
                chapter_data['description'] = chapter['description']

            chapters.append(chapter_data)

        data = {
            'title': book_data['title'],
            'art': static("{0}/{1}/{2}".format(settings.AUDIOBOOKS_DIRNAME, slug, book_data['album_art'])),
            'chapters': chapters
        }

        if book_data['description'] is not None:
            data['description'] = book_data['description']

        return data
