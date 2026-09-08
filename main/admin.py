from django.contrib import admin
from main.models import Experience, Skill, Project
# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)