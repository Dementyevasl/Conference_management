import django_tables2 as tables
from django_tables2.utils import A
import django_filters
from .models import Conference

class ConferenceTable(tables.Table):
    
    _ = tables.LinkColumn('conference:detail', text='See Below', args=[A('pk')], orderable=False, empty_values=())
    class Meta:
        model = Conference
        fields = ('confTitle', 'location_country', 'location_city', 'dates_start', 'dates_end', 'website')
        template_name = 'django_tables2/bootstrap.html'
