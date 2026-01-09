from django.shortcuts import render
from django.db.models import Sum
from contributions.models import Contribution
from members.models import Member

def dashboard_home(request):
    total_contributions = Contribution.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0

    total_members = Member.objects.count()

    return render(request, "dashboard/home.html", {
        "total_contributions": total_contributions,
        "total_members": total_members,
    })
