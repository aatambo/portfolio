from django.contrib import admin

from .models import Profile, Project, Quote

admin.site.register(Project)
admin.site.register(Quote)
admin.site.register(Profile)
