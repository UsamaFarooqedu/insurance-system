from django.db import models
from beneficiaries.models import Beneficiary

class Policy(models.Model):
    """Represents an insurance policy linked to a beneficiary."""
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='policies')
    policy_number = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Pending', 'Pending')],
        default='Pending'
    )

    def __str__(self):
        return f"Policy {self.policy_number} for {self.beneficiary}"