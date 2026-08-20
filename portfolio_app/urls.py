from django.urls import include, path
from rest_framework.routers import DefaultRouter

from portfolio_app.views import AddContact, ProjectViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")

urlpatterns = [
    path("", include(router.urls)),
    path("contacts/add/", AddContact.as_view(), name="add-contact"),
]
