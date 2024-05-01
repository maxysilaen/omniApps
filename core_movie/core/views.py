from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Movie
from .serializers import MovieSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
