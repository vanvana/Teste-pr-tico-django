from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Client(Model):
    name = models.CharField(max_length=50, verbose_name='nome', null=False)
    cpf = models.CharField(max_length=14, verbose_name='cpf', null=False)
    age = models.IntegerField(verbose_name='idade', null=False)
    
