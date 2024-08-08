from django.db import models

# Create your models here.

class MachineSpecs(models.Model):

    specs = models.JSONField()

    def __str__(self):
        return "Specs"