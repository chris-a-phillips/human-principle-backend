from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Principle
from .serializers import PrincipleSerializer
from rest_framework.permissions import IsAuthenticated
from human_principle_backend.permissions import IsOwner



class PrincipleViewSet(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        queryset = Principle.objects.filter(user=request.user)
        serializer = PrincipleSerializer(queryset, many=True)

        return  response.Response(serializer.data)