from django.db import models
from Company.models import CompanyModel, User
from device.models import DeviceModel
from Employee.models import EmployeeModel
from assetHistory.constants import HISTORY_TYPE

class AssetHistory(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ManyToManyField(DeviceModel)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, null=True, blank=True)
    historyType = models.IntegerField(choices=HISTORY_TYPE, null=True)
    is_returned = models.BooleanField(default=False)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    provide_date = models.DateTimeField(auto_now_add=True)
    condition_out = models.CharField(max_length=255, null=True, blank=True)
    condition_in = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Give device to {self.employee.name}'
    

    