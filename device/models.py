from django.db import models
from Company.models import CompanyModel

class DeviceModel(models.Model):
    model_name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=30)
    identification_no = models.CharField(max_length=30)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.model_name