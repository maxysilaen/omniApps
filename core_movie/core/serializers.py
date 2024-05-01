from rest_framework import serializers
from .models import Movie, Genre, MPAA_Rating

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class MPAA_RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MPAA_Rating
        fields = ('type', 'label')

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    mpaaRating = MPAA_RatingSerializer()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'imgPath', 'duration', 'genre', 'language', 'mpaaRating', 'userRating')
