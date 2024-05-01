from django.contrib import admin
from .models import Movie, Genre, MPAA_Rating


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MPAA_RatingAdmin(admin.ModelAdmin):
    list_display = ('type', 'label')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'language', 'get_genres', 'get_mpaa_rating', 'userRating')
    filter_horizontal = ('genre',)

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])

    get_genres.short_description = 'Genres'

    def get_mpaa_rating(self, obj):
        return f"{obj.mpaaRating.type} - {obj.mpaaRating.label}"

    get_mpaa_rating.short_description = 'MPAA Rating'


admin.site.register(Genre, GenreAdmin)
admin.site.register(MPAA_Rating, MPAA_RatingAdmin)
admin.site.register(Movie, MovieAdmin)