from django.contrib import admin
from .models import Exercise, BodyPart, Type, Equipment, Level


admin.site.register(BodyPart)
admin.site.register(Type)
admin.site.register(Equipment)
admin.site.register(Level)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_part', 'level')
    ordering = ('name',)
    search_fields = ('name',)