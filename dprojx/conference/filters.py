
import django_filters
from .models import Conference

class ConferenceFilter(django_filters.FilterSet):
    class Meta:
        model = Conference
        fields = ['confTitle']
        