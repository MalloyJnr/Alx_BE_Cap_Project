from rest_framework import viewsets, permissions
from .models import Contribution
from .serializers import ContributionSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render

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
    
    @action(detail=False, methods=["get"], url_path="summary-by-member")
    def summary_by_member(self, request):
        data = (
            Contribution.objects
            .values("member__id", "member__full_name")
            .annotate(total=Sum("amount"))
            .order_by("-total")
    )
        result = [
            {
                "member_id": item["member__id"],
                "member_name": item["member__full_name"],
                "total": item["total"]
            }
            for item in data
        ]

        return Response(result)

def contribution_type_totals(request):
    totals = Contribution.objects.values(
        "contribution_type"
    ).annotate(
        total=Sum("amount")
    )

    return render(request, "contributions/type_totals.html", {
        "totals": totals
    })

def contributions_list(request):
    contributions = Contribution.objects.select_related("member").order_by("-date")

    return render(request, "contributions/contributions_list.html", {
        "contributions": contributions
    })
