from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Tags)
admin.site.register(Users)
admin.site.register(Article)
admin.site.register(Comment)