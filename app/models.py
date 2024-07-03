from django.db import models

# Create your models here.
class staff(models.Model):
    name = models.CharField(max_length=100)
    s_id = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class customer(models.Model):
    c_name = models.CharField(max_length=100)
    c_id = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name
    
class record(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    s_name = models.CharField(max_length=100)
    c_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    matter = models.CharField(max_length=100)
    followup = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    Purpose = models.CharField(max_length=100)

    def __str__(self):
        return self.Purpose

