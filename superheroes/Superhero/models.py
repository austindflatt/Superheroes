from django.db import models

# Create your models here.


class SuperHeroes(models.Model):
    superhero_name = models.CharField
    alter_ego_name = models.CharField
    primary_ability = models.CharField
    secondary_ability = models.CharField
    catchphrase = models.CharField


    def __str__(self):
        return self.superhero_name
        return self.alter_ego_name
        return self.primary_ability
        return self.secondary_ability
        return self.catchphrase
