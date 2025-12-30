from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Contribution
from .serializers import ContributionSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    permission_classes = [IsAuthenticated]
