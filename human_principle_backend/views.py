from django.shortcuts import render
from rest_framework import viewsets
from .models import Principle
from .serializers import PrincipleSerializer
from rest_framework.permissions import IsAuthenticated
from human_principle_backend.permissions import IsOwner



class PrincipleViewSet(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        # if self.action == 'list' or self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
        #     permission_classes = [IsOwner]
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwner]

        return [permission() for permission in permission_classes]