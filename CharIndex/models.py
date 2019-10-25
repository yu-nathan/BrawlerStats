from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    char_name = models.CharField(max_length=200)

    def __str__(self):
        return self.char_name

class Stats(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    rarity = models.CharField(max_length=200)
    movement_speed = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    range = models.IntegerField(default=0)
    bullets_per_attack = models.IntegerField(default=0)
    dps = models.IntegerField(default=0)
    super_range = models.IntegerField(default=0)
    bullets_per_super = models.IntegerField(default=0)
    super_dps = models.IntegerField(default=0)

    def __str__(self):
        return "{}'s character stats.".format(self.character.char_name)
