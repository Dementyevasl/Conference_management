# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from dappx import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^dappx/', include('dappx.urls')),
    url(r'^conference/', include('conference.urls')),
    #path('conferences/', include('conference.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('profile/<int:pk>', views.UserDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('profile/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('about/', views.about, name='about'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('profile/reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('profile/reset_password/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('profile/reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('profile/reset_password/complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
# path('password_reset/', PasswordResetView.as_view(success_url='done/'), name="password_reset"),
# path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
# path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view( success_url='/accounts/reset/done/'), name="password_reset_confirm"),
# path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
