# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from authentication.models import  User
from django.db import models

# Create your models here.
class Expense(models.Model):
  CATEGORY_OPTIONS=[
    ('ONLINE_SERVICES','ONLINE_SERVICES'),
    ('TRAVEL','TRAVEL'),
    ('FOOD','FOOD'),
    ('RENT','RENT'),
    ('OTHERS','OTHERS')
  ]
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
  amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
  description = models.TextField()
  date = models.DateField(null=False, blank=False)
