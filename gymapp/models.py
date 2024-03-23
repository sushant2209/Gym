from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    membership_start_date = models.DateField(blank=True, null=True, default=None)
    membership_end_date = models.DateField(blank=True, null=True, default=None)
