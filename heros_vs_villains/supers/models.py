from django.db import models

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey("super_types.SuperType", on_delete=models.CASCADE) # Added the folder name and used dot notation for the Class Model Name