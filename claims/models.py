from django.db import models
from beneficiaries.models import Beneficiary

class Claim(models.Model):
    """Represents a claim submitted by a beneficiary."""
    claim_id = models.CharField(max_length=15, unique=True)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='claims')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_submitted = models.DateField(auto_now_add=True)
    priority = models.IntegerField(default=0)  # Higher value = higher priority
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )

    def __str__(self):
        return f"Claim {self.claim_id} by {self.beneficiary}"