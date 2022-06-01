from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=5)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    bloodgroup = models.CharField(max_length=10)

    def __init__(self):
        return self

# Create your models here.
