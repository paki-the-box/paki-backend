from django.db import models

# Create your models here.


class HandoverTransaction(models.Model):
    transactionId = models.CharField(max_length=255, null=False, blank=False)
    sending_contact = models.CharField(max_length=255, null=False, blank=False) # Mail of sender
    receiving_contact = models.CharField(max_length=255, null=False, blank=False)
    box_id = models.CharField(max_length=255, null=False, blank=False)
    size = models.CharField(max_length=255, choices=[('S', 'Small'), ('M', 'Medium'), ('L','Large')])
    accepted_by_receiver = models.BooleanField(null=True)
    transaction_state = models.CharField(max_length=255, null=False, choices=[('C', 'Created'), ('A', 'Accepted'), ('D', 'Denied'), ('DR', 'Dropped-Off'), ('PU','Picked-UP')])
    dropoff_date = models.DateField(null=False)
    pickup_date = models.DateField(null=True)
    

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
