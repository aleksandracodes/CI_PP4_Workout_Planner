# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from cloudinary.models import CloudinaryField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BodyPart(models.Model):
    """
    A class for the body part model
    """
    part = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Returns the body part name string
        """
        return self.part


class Type(models.Model):
    """
    A class for the exercise type model
    """
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Returns the exercise type string
        """
        return self.type


class Equipment(models.Model):
    """
    A class for the equipment model
    """
    equipment = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Returns the equipment type name string
        """
        return self.equipment


class Level(models.Model):
    """
    A class for the level model
    """
    level = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Returns the level name string
        """
        return self.level


class Exercise(models.Model):
    """
    A class for the exercise model
    """
    name = models.CharField(
        max_length=150,
        unique=True
    )
    description = models.TextField()
    body_part = models.ForeignKey(
        BodyPart,
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE
    )
    equipment = models.ManyToManyField(Equipment)
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE
    )
    image = CloudinaryField(
        'image',
        default='placeholder'
    )

    def __str__(self):
        """
        Returns the exercise name string
        """
        return self.name
