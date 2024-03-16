from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    company_name = models.CharField(max_length=70)
    

class CompanyModel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    registered_no = models.CharField(max_length=30)
    aboutCompany = models.TextField()
    contactInfo = models.TextField()
    location = models.CharField(max_length=100)
    numberOfEmployee = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.company_name