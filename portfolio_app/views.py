from rest_framework import viewsets

from portfolio_app.models import Project
from portfolio_app.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.select_related(
            "industry",
            "details",
        ).prefetch_related(
            "technologies",
            "features",
            "details__key_features",
            "details__challenges",
            "details__impacts",
        )
