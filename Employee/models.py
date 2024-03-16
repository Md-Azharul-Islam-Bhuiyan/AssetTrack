from django.db import models
from department.models import Department
from Company.models import CompanyModel

class EmployeeModel(models.Model):
      name = models.CharField(max_length=50)
      designation = models.CharField(max_length=30)
      department = models.ForeignKey(Department, on_delete=models.CASCADE)
      company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
      phone_no = models.CharField(max_length=11)
      email=models.EmailField()
      Address = models.TextField()

      def __str__(self):
        return self.name