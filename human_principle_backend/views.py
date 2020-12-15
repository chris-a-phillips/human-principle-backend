from django.shortcuts import render
from rest_framework import viewsets
from .models import Principle
from .serializers import PrincipleSerializer
from rest_framework.permissions import IsAuthenticated



class PrincipleViewSet(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
    permission_classes = [IsAuthenticated]