from rest_framework import viewsets, permissions
from .models import Claim
from .serializers import ClaimSerializer
from heapq import heappush, heappop

class ClaimViewSet(viewsets.ModelViewSet):
    """API endpoint for claims."""
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Process claims using a priority queue based on priority."""
        instance = serializer.save()
        priority_queue = []
        heappush(priority_queue, (-instance.priority, instance.id))  # Negative for max-heap
        if priority_queue:
            _, claim_id = heappop(priority_queue)
            claim = Claim.objects.get(id=claim_id)
            # Simplified logic: auto-approve high-priority claims
            if claim.priority >= 5:
                claim.status = 'Approved'
                claim.save()