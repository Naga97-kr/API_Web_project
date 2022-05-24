# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    user_id = models.CharField(max_length=30)
    pwd = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    addr = models.CharField(max_length=100)
    birth = models.IntegerField(default=0,validators=[MaxValueValidator(99999999),MinValueValidator(10000000)])
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Board(models.Model):
    title = models.CharField(max_length=20, null = True)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null = True)
# Create your models here.
