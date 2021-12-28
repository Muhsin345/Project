from django.db import models

# Create your models here.
class tblsignup(models.Model):
    Name=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=15)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)