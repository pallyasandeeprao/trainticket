from django.db import models

# Create your models here.
class Trains(models.Model):
    train_number=models.IntegerField()
    train_destination=models.CharField(max_length=100)
    no_of_tickets=models.IntegerField()
    date=models.DateField()
    amount=models.CharField(max_length=70)

    def __str__(self):
        return self.train_destination

class Ticket(models.Model):
    name=models.CharField(max_length=60)
    mobile=models.CharField(max_length=20)
    city=models.CharField(max_length=70)
    no_of_tickets=models.IntegerField()
