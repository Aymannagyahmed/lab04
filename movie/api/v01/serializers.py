from movie.models import Movie
from rest_framework import serializers
from cast.api.v01.serializers import CastSerializer
from category.api.v01.serializers import CategorySerializer

class MovieSerializer(serializers.ModelSerializer):
    casts = CastSerializer(many=True,read_only=True)
    categories = CategorySerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id',]