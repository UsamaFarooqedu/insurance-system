from django.contrib import admin
from .models import Beneficiary

@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ['insurance_id', 'first_name', 'last_name', 'date_of_birth', 'region']
    search_fields = ['insurance_id', 'first_name', 'last_name']