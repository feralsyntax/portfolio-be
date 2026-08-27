from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from portfolio_app.models import Project
from portfolio_app.serializers import ContactSerializer, ProjectSerializer
from portfolio_app.services import send_new_contact_email


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
@method_decorator(never_cache, name="list")
@method_decorator(never_cache, name="retrieve")
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]  # noqa: RUF012
    lookup_field = "uuid"

    def get_queryset(self):
        return (
            Project.objects.select_related(
                "industry",
                "details",
            )
            .prefetch_related(
                "technologies",
                "features",
                "details__key_features",
                "details__challenges",
                "details__impacts",
            )
            .order_by("-is_featured", "-first_created")
        )


class AddContact(APIView):
    permission_classes = [permissions.AllowAny]  # noqa: RUF012

    @extend_schema(
        tags=["Contact"],
        operation_id="addContact",
        summary="Add a new contact and message admin",
        description=(
            "Add a new contact to the database"
            "And send an email message to the portfolio admin."
        ),
        auth=[],
        request=ContactSerializer,
        responses={
            201: OpenApiResponse(
                response=ContactSerializer,
                description="A new contact instance has been created.",
            )
        },
    )
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contact = serializer.save()

        send_new_contact_email(contact)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
