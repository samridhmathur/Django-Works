from django.db import models

# Create your models here.
class Employee(models.Model):
    # Adding Fields for Employee
    employeeId = models.IntegerField(primary_key=True,null=False)
    firstName = models.CharField(max_length=255,null=False)
    lastName = models.CharField(max_length=255,null=False)
    phone = models.CharField(max_length=12,null=False)
    email = models.EmailField(max_length=255,null=False)

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.employeeId,self.firstName,self.lastName,self.phone,self.email)
