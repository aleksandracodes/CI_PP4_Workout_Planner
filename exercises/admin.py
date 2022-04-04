# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
from .models import Exercise, BodyPart, Type, Equipment, Level
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


admin.site.register(BodyPart)
admin.site.register(Type)
admin.site.register(Equipment)
admin.site.register(Level)


@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    """
    Admin class for the Exercise model
    """
    list_display = (
        'name',
        'body_part',
        'level')
    ordering = ('name',)
    search_fields = ('name',)
    summernote_fields = ('description')