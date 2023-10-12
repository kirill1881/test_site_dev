from django.contrib import admin
from .models import *


class TestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Subject, SubjectAdmin)
