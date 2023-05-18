from django.contrib import admin

from .models import Posts, Category

admin.site.register(Category)
admin.site.register(Posts)
