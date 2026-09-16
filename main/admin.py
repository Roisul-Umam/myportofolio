from django.contrib import admin
from main.models import Experience, Skill, Project
from main.forms import SkillForm
# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    form = SkillForm

admin.site.register(Skill, SkillAdmin)
admin.site.register(Project)
admin.site.register(Experience)