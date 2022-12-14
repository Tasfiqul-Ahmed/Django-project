from django.db import models

# Create your models here.
class Donor(models.Model):
    d_id = models.TextField(max_length=20, primary_key=True)
    profile_no = models.IntegerField(max_length=10)
    d_availablity = models.CharField(max_length=5)
    d_last_donation_date = models.FloatField(max_length=10)

class receiver(models.Model):
    rec_id = models.TextField(max_length=20, primary_key=True)
    profile_no = models.TextField(max_length=20)
    rec_contact = models.IntegerField(max_length=15)
