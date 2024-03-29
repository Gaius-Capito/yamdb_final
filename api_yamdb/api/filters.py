from django_filters import rest_framework as filter_

from reviews.models import Title


class TitleFilter(filter_.FilterSet):
    genre = filter_.CharFilter(
        field_name='genre__slug',
        lookup_expr='exact'
    )
    category = filter_.CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    name = filter_.CharFilter()
    year = filter_.CharFilter()

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')
