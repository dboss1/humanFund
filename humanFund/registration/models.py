from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fName = models.CharField(max_length=20)
    mName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    cellPhone = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    dob = models.DateField()
    
class login(models.Model):
    test = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

class portal(models.Model):
    office = models.CharField(max_length=20)
    officer = models.CharField(max_length=20)
    org = models.CharField(max_length=20)
    orgMember = models.CharField(max_length=20)
    subscriber = models.CharField(max_length=20)