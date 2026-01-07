from rest_framework import viewsets, permissions
from .models import Contribution
from .serializers import ContributionSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all().order_by("-date")
    serializer_class = ContributionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
