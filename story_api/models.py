from django.db import models
class Story(models.Model):
    health = models.IntegerField()
    attack = models.IntegerField()
    accuracy = models.IntegerField()
    weapons = models.JSONField()
    items = models.JSONField()
    villains = models.JSONField()
	