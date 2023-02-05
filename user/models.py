from django.db import models


class User(models.Model):
    major = models.CharField(max_length=100, blank=True, default="")
    sg_type = models.CharField(max_length=100, blank=True, default="")
