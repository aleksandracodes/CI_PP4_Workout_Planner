from django.db import models
from cloudinary.models import CloudinaryField



class BodyPart(models.Model):
    part = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.part


class Type(models.Model):
    type = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.type


class Equipment(models.Model):
    equipment = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.equipment


class Level(models.Model):
    level = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.level


class Exercise(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    equipment = models.ManyToManyField(Equipment)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name