from rest_framework import serializers
from django.db.models import Sum
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    total_dues = serializers.SerializerMethodField()
    total_welfare = serializers.SerializerMethodField()
    total_offering = serializers.SerializerMethodField()
    total_contributions = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = "__all__"

    def get_total_dues(self, obj):
        return obj.contributions.filter(
            contribution_type="DUES"
        ).aggregate(total=Sum("amount"))["total"] or 0

    def get_total_welfare(self, obj):
        return obj.contributions.filter(
            contribution_type="WELFARE"
        ).aggregate(total=Sum("amount"))["total"] or 0

    def get_total_offering(self, obj):
        return obj.contributions.filter(
            contribution_type="OFFERING"
        ).aggregate(total=Sum("amount"))["total"] or 0

    def get_total_contributions(self, obj):
        return obj.contributions.aggregate(
            total=Sum("amount")
        )["total"] or 0
