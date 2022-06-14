from django.db import models

# Create your models here.
class Subscribe(models.Model):
    email_address =models.CharField(max_length=80)
    first_name =models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name