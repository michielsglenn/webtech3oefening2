from __future__ import unicode_literals

from django.db import models



# Create your models here.

class examen(models.Model):
	examen_naam = models.CharField(max_length=50)
	examen_date = models.DateTimeField()
	examen_student = models.CharField(max_length=50)
	examen_reden = models.CharField(max_length=200)
	
	