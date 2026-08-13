from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, viewsets

from portfolio_app.models import Project
from portfolio_app.serializers import ProjectSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List projects",
        description="Returns all portfolio projects.",
        responses=ProjectSerializer(many=True),
    ),
    retrieve=extend_schema(
        summary="Retrieve a project",
        description="Returns a single portfolio project by UUID.",
        responses=ProjectSerializer,
    ),
)
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
