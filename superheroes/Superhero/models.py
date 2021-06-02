from django.db import models

# Create your models here.


class SuperHeroes(models.Model):
    superhero_name = models.CharField
    alter_ego_name = models.CharField
    primary_ability = models.CharField
    secondary_ability = models.CharField
    catchphrase = models.CharField
