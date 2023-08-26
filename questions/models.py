from django.db import models
from datetime import datetime
# Create your models here.


class Question(models.Model):
    statement = models.CharField(max_length=5000)
    level = models.CharField(max_length=20)
    approach = models.CharField(max_length=50000)
    solution = models.CharField(max_length=50000)
    date_added = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.statement
