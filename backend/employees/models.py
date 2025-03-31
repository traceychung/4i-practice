from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    bio = models.CharField(max_length=2000)
    union_member = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
