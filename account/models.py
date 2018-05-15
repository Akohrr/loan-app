from django.db import models
from django.conf import settings
# from loan.models import Loan

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    salary = models.IntegerField()


    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)
