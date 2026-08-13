from rest_framework import permissions, viewsets

from portfolio_app.models import Project
from portfolio_app.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]  # noqa: RUF012
    lookup_field = "uuid"

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
