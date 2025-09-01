from rest_framework import serializers
from .models import Policy
from beneficiaries.models import Beneficiary

class PolicySerializer(serializers.ModelSerializer):
    """Serializer for Policy model."""
    beneficiary_id = serializers.PrimaryKeyRelatedField(
        queryset=Beneficiary.objects.all(), source='beneficiary'
    )

    class Meta:
        model = Policy
        fields = ['id', 'beneficiary_id', 'policy_number', 'start_date', 'end_date', 'premium', 'status']
        read_only_fields = ['status']

    def validate(self, data):
        """Ensure end_date is after start_date."""
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data