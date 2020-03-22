from django.contrib.auth.models import User
import django_filters
from .models import com_pro

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = com_pro
        fields = ['com_username', 'com_desc', 'com_place', 'com_pincode', 'com_dt', 'com_state', 'com_email' ,'com_mob' , 'com_country', ]
        