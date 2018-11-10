# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona (models.Model):
    Nombre = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=40)
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField()
    Domicilio = models.CharField(max_length=50)