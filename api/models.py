from django.db import models

class JobApplicant(models.Model):
	first_name = models.TextField();
	last_name = models.TextField();
	email = models.EmailField();
	phone = models.TextField();
	address = models.TextField();

	def __str__(self):
		return self.first_name+" "+self.last_name;
