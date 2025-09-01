from rest_framework import serializers
from .models import Claim
from beneficiaries.models import Beneficiary

class ClaimSerializer(serializers.ModelSerializer):
    """Serializer for Claim model."""
    beneficiary_id = serializers.PrimaryKeyRelatedField(
        queryset=Beneficiary.objects.all(), source='beneficiary'
    )

    class Meta:
        model = Claim
        fields = ['id', 'claim_id', 'beneficiary_id', 'amount', 'date_submitted', 'priority', 'status']
        read_only_fields = ['date_submitted', 'status']

    def validate_amount(self, value):
        """Ensure claim amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Claim amount must be positive.")
        return value