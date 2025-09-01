from django.views.generic import ListView
from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Beneficiary
from .serializers import BeneficiarySerializer

class BeneficiaryListView(ListView):
    """Web view for listing beneficiaries."""
    model = Beneficiary
    template_name = 'beneficiaries/beneficiary_list.html'
    context_object_name = 'beneficiaries'

    def get_queryset(self):
        """Optimize query with search functionality."""
        queryset = Beneficiary.objects.all()
        search_term = self.request.GET.get('search', '')
        if search_term:
            queryset = queryset.filter(
                Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term)
            )
        return queryset

class BeneficiaryViewSet(viewsets.ModelViewSet):
    """API endpoint for beneficiaries."""
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Custom filtering using DSA (hash-based lookup for insurance_id)."""
        queryset = super().get_queryset()
        insurance_id = self.request.query_params.get('insurance_id')
        if insurance_id:
            return queryset.filter(insurance_id=insurance_id)
        return queryset