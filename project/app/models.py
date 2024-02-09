from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class studentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    marks = models.FloatField( validators=[MinValueValidator(0),MaxValueValidator(100)])
