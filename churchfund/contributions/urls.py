from rest_framework.routers import DefaultRouter
from .views import ContributionViewSet
from django.urls import path
from contributions.views import contribution_type_totals, contributions_list, create_contribution

router = DefaultRouter()
router.register(r"contributions", ContributionViewSet, basename="contribution")

urlpatterns = [
    path("contributions/totals/", contribution_type_totals, name="contribution-type-totals"),
    path("contributions/", contributions_list, name="contributions-list"),
    path("contributions/create/", create_contribution, name="contribution-create"),
]

urlpatterns += router.urls
