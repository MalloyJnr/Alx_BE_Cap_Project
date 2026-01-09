from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Member
from .serializers import MemberSerializer
from django.shortcuts import render, redirect
from .models import Member
from contributions.models import Contribution
from django.db.models import Sum

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]


def members_list(request):
    members = Member.objects.all().order_by("full_name")
    return render(request, "members/list.html", {"members": members})

def create_member(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        Member.objects.create(
            full_name=full_name,
            phone=phone,
            email=email
        )
        return redirect("members-list")

    return render(request, "members/create.html")

def member_contribution_totals(request):
    members = Member.objects.all()

    rows = []
    for m in members:
        total = Contribution.objects.filter(
            member=m
        ).aggregate(total=Sum("amount"))["total"] or 0

        rows.append({
            "name": m.full_name,
            "total": total
        })

    return render(request, "members/member_totals.html", {
        "rows": rows
    })