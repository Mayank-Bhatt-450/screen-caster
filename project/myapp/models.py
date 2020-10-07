from django.db import models

# Create your models here.
class data_m(models.Model):
    data=models.TextField()
    def __str__(self):
        return self.data
