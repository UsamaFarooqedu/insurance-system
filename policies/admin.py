from django.contrib import admin
from .models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['policy_number', 'beneficiary', 'start_date', 'end_date', 'status']
    search_fields = ['policy_number', 'beneficiary__insurance_id']