from django.contrib import admin
from .models import BanClass,StudentInfo,StudentDetail

# Register your models here.
admin.site.register(BanClass)
admin.site.register(StudentInfo)
admin.site.register(StudentDetail)