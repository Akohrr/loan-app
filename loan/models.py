from django.db import models
from account.models import Profile

# Create your models here.

class Loan(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined')
    )
    #user that maked the request
    author = models.ForeignKey(Profile, related_name='loan_author')
    #amount of money to borrow
    amount = models.IntegerField()
    #amount of money to pay in installments
    installments = models.IntegerField(help_text='Amount to pay in monthly installments')
    #guarantor to accept/decline loan request
    guarantor = models.OneToOneField(Profile, related_name='loan_guarantor')
    #status of the loan request
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    #date loan request is made
    date_of_request = models.DateTimeField(auto_now_add=True)
    #date admin personnel confirms/decline loan request
    date_of_confirmation = models.DateTimeField(blank=True, null=True)

