from django.db import models

class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField()

    def __str__(self):
        return self.full_name
