from rest_framework import serializers
from .models import Beneficiary

class BeneficiarySerializer(serializers.ModelSerializer):
    """Serializer for Beneficiary model."""
    age = serializers.ReadOnlyField()

    class Meta:
        model = Beneficiary
        fields = ['id', 'insurance_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'region', 'age', 'created_at']
        read_only_fields = ['created_at', 'age']

    def validate_insurance_id(self, value):
        """Custom validation for insurance_id."""
        if Beneficiary.objects.filter(insurance_id=value).exists():
            raise serializers.ValidationError("Insurance ID must be unique.")
        return value