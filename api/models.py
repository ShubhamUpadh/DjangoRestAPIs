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
