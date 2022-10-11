from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import VPSSerializer
from .models import VPS


class VPSView(ModelViewSet):
    serializer_class = VPSSerializer
    queryset = VPS.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'status',
        'ram',
        'hdd',
        'uid',
        'cpu',
    ]

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = VPS.objects.get(uid=kwargs.get("uid"))
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        except VPS.DoesNotExist:
            return Response(status=404, data={
                "message": "Server does not exist"
            })

    def get_current_server(self, request, *args, **kwargs):
        try:
            instance = VPS.objects.get(uid=kwargs.get("uid"))
            return Response(self.serializer_class(instance, many=False).data)
        except VPS.DoesNotExist:
            return Response(status=404, data={
                "message": "Server does not exist"
            })

