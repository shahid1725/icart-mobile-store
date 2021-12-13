import django_filters
from .models import Phone,Order

class PhoneFilter(django_filters.FilterSet):
    class Meta:
        model=Phone
        fields=["Name","Color","Price","Copies"]

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Order
        fields=["item","user","order_date","status"]