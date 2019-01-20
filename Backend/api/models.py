from django.db import models
from picklefield.fields import PickledObjectField
# Create your models here.

class MLModel(models.Model):
    ml_model = PickledObjectField()