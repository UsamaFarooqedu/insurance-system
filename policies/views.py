from rest_framework import viewsets, permissions
from .models import Policy
from .serializers import PolicySerializer
from heapq import heappush, heappop
from datetime import date

class PolicyViewSet(viewsets.ModelViewSet):
    """API endpoint for policies."""
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Custom create with priority queue for processing urgent policies."""
        instance = serializer.save()
        priority_queue = []
        heappush(priority_queue, (instance.start_date, instance.id))
        if priority_queue:
            _, policy_id = heappop(priority_queue)
            policy = Policy.objects.get(id=policy_id)
            if policy.start_date <= date.today():
                policy.status = 'Active'
                policy.save()