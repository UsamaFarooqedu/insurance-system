from django.contrib import admin
from .models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['claim_id', 'beneficiary', 'amount', 'priority', 'status']
    search_fields = ['claim_id', 'beneficiary__insurance_id']