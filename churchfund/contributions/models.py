from django.db import models
from members.models import Member

class Contribution(models.Model):
    CONTRIBUTION_TYPES = [
        ("dues", "Church Dues"),
        ("welfare", "Welfare"),
        ("offering", "Offering"),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="contributions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contribution_type = models.CharField(max_length=20, choices=CONTRIBUTION_TYPES)
    date = models.DateField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member} - {self.contribution_type}"
