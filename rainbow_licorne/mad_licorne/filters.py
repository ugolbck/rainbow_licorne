from django_filters import FilterSet, CharFilter
from mad_licorne.models import Article


class ArticleFilter(FilterSet):
	title = CharFilter(lookup_expr='icontains')

	class Meta:
		model = Article
		fields = ['title', ]
