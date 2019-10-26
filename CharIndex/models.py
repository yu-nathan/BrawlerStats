from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    def get_image_path(instance, filename):
        return '{0}/{1}'.format(instance.char_origin, filename)

    char_name = models.CharField('character name', max_length=200)
    char_img = models.ImageField(upload_to=get_image_path, blank=False, null=True)
    char_origin = models.CharField('character origin', max_length=200)
    pub_date = models.DateTimeField('date created')

    def __str__(self):
        return self.char_name

class Stats(models.Model):
    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        primary_key=True)
    rarity = models.CharField('Rarity', max_length=200)
    movement_speed = models.IntegerField('Movement speed', null=True)
    health = models.IntegerField('Health', null=True)
    range = models.DecimalField('Range', null=True, max_digits=4, decimal_places=2)
    reload_speed = models.DecimalField('Reload speed', null=True, max_digits=4, decimal_places=2)
    bullets_per_attack = models.IntegerField('Bullets per attack', null=True)
    damage_per_bullet = models.IntegerField('Damage per bullet', null=True)
    super_range = models.DecimalField('Super range', null=True, max_digits=4, decimal_places=2)
    bullets_per_super = models.IntegerField('Bullets per super', null=True)
    super_damage_per_bullet = models.IntegerField('Super damage per bullet', null=True)

    def get_fields(self):
        print(Stats._meta.fields[0].__dict__.keys())
        return [(field.verbose_name, field.value_to_string(self)) for field in Stats._meta.fields]

    def __str__(self):
        return "{}'s character stats.".format(self.character.char_name)
