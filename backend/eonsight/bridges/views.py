from rest_framework import generics
from .models import Bridge
from .serializers import BridgeSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


class BridgeViewSet(viewsets.ModelViewSet):
    queryset = Bridge.objects.all()
    serializer_class = BridgeSerializer

    def retrieve(self, request, *args, **kwargs):
        bridge = self.get_object()
        serializer = self.serializer_class(bridge)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        bridge = self.get_object()
        serializer = self.serializer_class(bridge, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        bridge = self.get_object()
        bridge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
