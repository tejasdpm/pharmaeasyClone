from django.contrib.auth.models import User
from django.db import models

class Customer(User):
    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
        ('O', "Others")
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

class Prescription(models.Model):
    image_url = models.CharField(max_length=200)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
