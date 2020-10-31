from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        db_table = 'paki_backend_users'
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique email')
        ]
