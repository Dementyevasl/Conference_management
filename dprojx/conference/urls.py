from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'conference'

urlpatterns = [
    path('management_page/', views.management_page, name = 'management_page'),
    # ex: /conferences/
    path('conferences/', views.listing, name='index'),
    # ex: /conferences/5/
    path('conferences/<int:conference_id>/', views.detail, name='detail'),
]