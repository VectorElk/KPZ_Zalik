#-*- coding: utf-8 -*-
from django.db import models
from livestock.models import *

# Create your models here.


class Respondent(models.Model):
    name = models.CharField("Name", primary_key=True, max_length=45)
    business_adress = models.CharField("Judical location", max_length=45, default="Somewhere")
    actual_adress = models.CharField("Physical adress", max_length=45, default="Somewhere else?")

    def __str__(self):
        return str(self.name)


class LivestockProduction(models.Model):
    name = models.CharField("Name", primary_key=True, max_length=45)
    unit = models.CharField("Unit", max_length=45)
    amount = models.PositiveIntegerField("Amount")
    id = models.ForeignKey(Respondent, models.CASCADE)

    def __str__(self):
        return str(self.name)


class CattleAndPoultry(models.Model):
    name = models.CharField("Назва показника", primary_key=True, max_length=45)
    cattle = models.PositiveIntegerField("Cattle")
    pigs = models.PositiveIntegerField("Pig")
    sheep_goat = models.PositiveIntegerField("Sheep and goat")
    horses = models.PositiveIntegerField("Horses")
    poultr = models.PositiveIntegerField("Poutry")
    id = models.ForeignKey(Respondent, models.CASCADE)

    def __str__(self):
        return str(self.name)


class Poultry(models.Model):
    name = models.CharField("Name", primary_key=True, max_length=45)
    adult = models.PositiveIntegerField("Adult")
    young = models.PositiveIntegerField("Young")
    cattle_and_poultry_id = models.ForeignKey(CattleAndPoultry, models.CASCADE)

    def __str__(self):
        return str(self.name)

