from django.db import models


# Create your models here.

# Creating company models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT', 'IT'),
                                                    ('Non IT', 'Non IT'),
                                                    ('Mobile Phone', 'Mobile Phones')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()

# Creating Employee Models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    phone= models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('Manager','Manager'),
                                                       ('Software Dev','SDE'),
                                                       ('Project Leader','PL')))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    objects = models.Manager()