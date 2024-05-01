import json
from django.core.management.base import BaseCommand
from core.models import Movie, Genre, MPAA_Rating

class Command(BaseCommand):
    help = 'Initiates data based on provided JSON'

    def handle(self, *args, **kwargs):
        with open('movies.json') as f:
            movies_data = json.load(f)

        for movie_data in movies_data:
            mpaa_rating_data = movie_data.pop('mpaaRating')
            mpaa_rating, _ = MPAA_Rating.objects.get_or_create(
                type=mpaa_rating_data['type'],
                label=mpaa_rating_data['label']
            )

            genres_data = movie_data.pop('genre')
            genres = []
            for genre_name in genres_data:
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                genres.append(genre)

            movie = Movie.objects.create(mpaaRating=mpaa_rating, **movie_data)
            movie.genre.set(genres)

        self.stdout.write(self.style.SUCCESS('Data initiated successfully'))
