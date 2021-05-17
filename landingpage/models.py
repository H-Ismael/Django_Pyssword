from django.db import models

class PassStrC(models.Model):

	passToCheck = models.CharField(max_length = 30)
	timeChecked = models.DateTimeField()
	passstrenght = models.CharField(max_length = 120, default = "No password to check")
	#dfdf
	
	def __str__(self):
		return self.passstrenght
		
# Create your models here.