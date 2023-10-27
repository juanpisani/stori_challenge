from django.db import models

from transaction_processor.enums import TransactionTypes


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=20, choices=TransactionTypes.choices())
    date = models.DateField()
    amount = models.FloatField()
