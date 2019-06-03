from django.urls import path

from . import views

app_name = 'conference'

urlpatterns = [
    # ex: /conferences/
    path('', views.index, name='index'),
    # ex: /conferences/5/
    path('<int:conference_id>/', views.detail, name='detail'),
]