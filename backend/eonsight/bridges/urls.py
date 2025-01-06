from django.urls import path
from .views import BridgeViewSet

urlpatterns = [
    path("bridges/", BridgeViewSet.as_view({"get": "list"}), name="bridge-list"),
    path(
        "bridges/details/<int:pk>/",
        BridgeViewSet.as_view({"get": "retrieve"}),
        name="bridge-detail",
    ),
    path("bridges/create/", BridgeViewSet.as_view({"post": "create"}), name="bridge-create"),
    path(
        "bridges/update/<int:pk>/",
        BridgeViewSet.as_view({"put": "update"}),
        name="bridge-update",
    ),
    path(
        "bridges/delete/<int:pk>/",
        BridgeViewSet.as_view({"delete": "destroy"}),
        name="bridge-delete",
    ),
]
