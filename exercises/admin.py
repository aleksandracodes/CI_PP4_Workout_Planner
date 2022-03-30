from django.contrib import admin
from .models import Exercise, BodyPart, Type, Equipment, Level


admin.site.register(Exercise)
admin.site.register(BodyPart)
admin.site.register(Type)
admin.site.register(Equipment)
admin.site.register(Level)