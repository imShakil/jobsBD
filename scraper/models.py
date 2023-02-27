from django.db import models


# Create your models here.


class Company(models.Model):
    companyName = models.CharField(max_length=140)
    companyLink = models.URLField()
    companyAddress = models.CharField(max_length=260)
    companySize = models.IntegerField()
    companyVacancy = models.IntegerField()


class Jobs(models.Model):
    companyId = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    link = models.URLField()
    salary = models.IntegerField()
    experiences = models.IntegerField()
    created_at = models.DateTimeField()
    deadline = models.DateTimeField()
    skills = models.CharField(max_length=260)

