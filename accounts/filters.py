import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CoronaFilter(django_filters.FilterSet):
	#start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	#end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	district_name = CharFilter(field_name='district_name',lookup_expr='icontains')

	class Meta:
		model = CoronaVirus
		fields = ['district_name']
		#exclude = ['customar', 'date_created']