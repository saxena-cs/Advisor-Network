from django.db import models

# Create your models here.
class Advisormodel(models.Model):
    name = models.CharField(max_length=100)
    profile_url = models.URLField(max_length=500)

    def __str__(self):
      return self.name
