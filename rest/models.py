from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    employeeId = models.IntegerField() 

    def __str__(self):
        return self.firstname
