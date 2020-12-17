from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Principle
from .serializers import PrincipleSerializer
from rest_framework.permissions import IsAuthenticated
from human_principle_backend.permissions import IsOwner



class PrincipleViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipleSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Principle.objects.all()
        else:
            queryset = Principle.objects.filter(user=self.request.user)

        return queryset
