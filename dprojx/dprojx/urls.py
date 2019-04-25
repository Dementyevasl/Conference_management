# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from dappx import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^dappx/', include('dappx.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('profile/', views.UserDetailView.as_view(), name='profile'),
    path('about/', views.about, name='about'),
]
