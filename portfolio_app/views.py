from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import permissions, viewsets

from portfolio_app.models import Project
from portfolio_app.serializers import ProjectSerializer


@extend_schema_view(
    list=extend_schema(
        tags=["Projects"],
        operation_id="projectsList",
        summary="List projects",
        description="List all portfolio projects with their details.",
        auth=[],
        responses={
            200: OpenApiResponse(
                response=ProjectSerializer(many=True),
                description="A list of portfolio projects.",
            )
        },
    ),
    retrieve=extend_schema(
        tags=["Projects"],
        operation_id="projectsRetrieve",
        summary="Retrieve a project",
        description="Retrieve a single portfolio project by UUID.",
        auth=[],
        responses={
            200: OpenApiResponse(
                response=ProjectSerializer,
                description="The requested portfolio project.",
            )
        },
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
