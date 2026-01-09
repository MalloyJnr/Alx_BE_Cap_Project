from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, members_list, create_member, member_contribution_totals

router = DefaultRouter()
router.register(r"members", MemberViewSet)

urlpatterns = [
    # Frontend pages
    path("members/", members_list, name="members-list"),
    path("members/create/", create_member, name="member-create"),
    path("members/totals/", member_contribution_totals, name="member-totals"),
]

# Add API routes
urlpatterns += router.urls
