from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'conference'

urlpatterns = [
    path('management_page/', views.management_page, name='management_page'),
    # ex: /conferences/
    path('list/', views.listing, name='index'),
    # ex: /conferences/5/
    path('<int:conference_id>/', views.detail, name='detail'),
    # ex: /submission/delete/1/
    path('submission/delete/<int:submission_id>/', views.delete_submission, name='delete_submission'),
    # ex: /submission/1/status/Accepted
    path('submission/<int:conference_id>/status/<str:status>',
         views.change_submission_status, name='change_submission_status'),
    # ex: /notifications/
    path('notifications/', views.list_notifications, name='list_notifications'),
    # ex: /notifications/
    path('notifications/<int:notification_id>', views.mark_read_notification, name='mark_read_notification'),
]