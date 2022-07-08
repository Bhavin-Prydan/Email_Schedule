from django.db import models

# Create your models here.
class Employee(models.Model):
	Id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=100)
	Email = models.EmailField()
	BirthDay = models.DateField()

	def __str__(self):
		return self.Name
