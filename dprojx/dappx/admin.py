# dappx/admin.py
from django.contrib import admin
from dappx.models import UserProfileInfo, User, Subject, Article, Author
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Subject)
admin.site.register(Article)
admin.site.register(Author)
