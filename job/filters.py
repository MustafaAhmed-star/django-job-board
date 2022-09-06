import django_filters
from .models import Job
from django_filters import rest_framework as filters
#class JobFilter(django_filters.FilterSet):
    #class Meta:
      #  model = Job
      ##  exclude= ['image','description',   'published_at','slug','experience','salary','owner','vacancy']




class JobFilter(filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude= ['image','description',   'published_at','slug','experience','salary','owner','vacancy']