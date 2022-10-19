from django.db import models

# Create your models here.

class Todos(models.Model):
    task = models.TextField()
    priority = models.IntegerField()
    date = models.DateField()
    completed = models.BooleanField(False)

    def __str__(self):
        return self.task