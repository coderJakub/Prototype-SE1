from django.db import models

class VM(models.Model):
    nameVM = models.CharField(max_length=30)