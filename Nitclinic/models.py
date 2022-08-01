from django.db import models


# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=30)
    checkup_category=models.CharField(max_length=59)
    appointment_date=models.DateField()
    class Meta:
        db_table="patient"
class user_login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=34)
    class Meta:
        db_table="user_login"
