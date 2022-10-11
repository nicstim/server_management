from django.urls import path
from .views import VPSView

app_name = "server"

urlpatterns = [
    path("", VPSView.as_view({
        "get": "list",
        "post": "create"
    })),
    path("<str:uid>/", VPSView.as_view({
        "get": "get_current_server",
        "patch": "partial_update"
    })),
]
