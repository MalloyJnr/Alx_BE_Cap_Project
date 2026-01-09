from rest_framework import viewsets, permissions
from .models import Contribution
from .serializers import ContributionSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all().order_by("-date")
    serializer_class = ContributionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    @action(detail=False, methods=['get'], url_path='summary-by-type')   
    def summary_by_type(self, request):
        data = (
        Contribution.objects
        .values('contribution_type')
        .annotate(total_amount=Sum('amount'))
        )
        results = {item['contribution_type']: item['total_amount'] for item in data}   
        return Response(results)
